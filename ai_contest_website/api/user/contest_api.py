from api.models import Contest, User
from api.serializers.ContestSerializer import ContestSerializer
from .serializers import UserContestRegisterSerializer
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.Contest import Contestant


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
            return Response({'message': 'Already registered'}, status=status.HTTP_400_BAD_REQUEST)
        contestant = Contestant(contest=contest, user=user, total_score=0)
        contestant.save()
        contest.attended_contestants.add(contestant)
        user.attended_contests.add(contestant)
        return Response({'message': 'Register successfully'}, status=status.HTTP_201_CREATED)
        

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