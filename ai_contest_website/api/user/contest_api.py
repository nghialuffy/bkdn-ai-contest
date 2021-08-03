from api.models import Contest, User
from api.serializers.ContestSerializer import ContestSerializer
from .serializers.contest_serializers import UserContestRegisterSerializer
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.Contest import Contestant
from api.utils import time_utils

class UserContestList(generics.GenericAPIView):
    """
    Get all the contest of a user
    """
    def get_contest(self, list_contest, contest_status: str):
        new_contests = []
        for contest in list_contest:
            time_start = contest.time_start
            time_end = contest.time_end
            if time_utils.get_status_contest(time_start, time_end) == contest_status:
                new_contests.append(contest)
        return new_contests

    def get(self, request, format=None):
        contest_status = request.GET.get('status', None)
        data = Contest.objects.all()
        if contest_status is not None:
            data = self.get_contest(data, contest_status)
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = ContestSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ContestSerializer(data, many=True)
        return Response(serializer.data)
        
            
class UserContestRegister(APIView):
    """
    Register a user to a contest.
    """
    def post(self, request, *args, **kwargs):
        contest_id = kwargs.get('contest_id')
        contest = Contest.objects.get(_id=contest_id)
        # # if contest.status != 'ongoing' or contest.status != 'upcoming':
        # #     return Response({'message': 'Cannot register this contest'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(_id=request.user.id)
        print(contest.__dict__)
        
        if Contestant.objects.filter(contest_id=contest_id, user=user).exists():
            return Response({'status': 'fail', 'message': 'Already registered'}, status=status.HTTP_200_OK)
        contestant = Contestant(contest=contest, user=user, total_score=0)
        contestant.save()
        contest.attended_contestants.add(contestant)
        user.attended_contests.add(contestant)
        return Response({'status': 'success', 'message': 'Register successfully'}, status=status.HTTP_201_CREATED)
        

class UserContestUnregister(APIView):
    """
    Register a user to a contest.
    """
    def post(self, request, *args, **kwargs):
        contest_id = kwargs.get('contest_id')
        contest = Contest.objects.get(_id=contest_id)
        # if contest.status != 'ongoing' or contest.status != 'upcoming':
        #     return Response({'message': 'Cannot register this contest'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(_id=request.user.id)
        try:
            contestant = Contestant.objects.get(user=user, contest=contest)
            print(contestant.__dict__)
            if contestant is not None:
                contest.attended_contestants.remove(contestant)
                user.attended_contests.remove(contestant)
                contestant.delete()

                return Response({'message': 'Unregister successfully'}, status=status.HTTP_201_CREATED)
            return Response({'message': 'You is not a contestant'}, status=status.HTTP_201_CREATED)
        except Contestant.DoesNotExist:
            return Response({'message': 'You is not a contestant'}, status=status.HTTP_201_CREATED)