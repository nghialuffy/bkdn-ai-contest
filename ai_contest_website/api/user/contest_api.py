from api.models import Contest, User
from api.serializers.ContestSerializer import ContestSerializer
from .serializers import UserContestRegisterSerializer
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class UserContestRegister(APIView):
    """
    Register a user to a contest.
    """
    def post(self, request, *args, **kwargs):
        contest_id = kwargs.get('contest_id')
        contest = Contest.objects.get(_id=contest_id)
        # if contest.status != 'ongoing' or contest.status != 'upcoming':
        #     return Response({'message': 'Cannot register this contest'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(_id=request.user.id)
        if contest.attended_contestants.filter(_id=user._id).exists():
            return Response({'message': 'Already registered'}, status=status.HTTP_400_BAD_REQUEST)
        contest.attended_contestants.add(user)
        user.attended_contests.add(contest)
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
        if contest.attended_contestants.filter(_id=user._id).exists():
            contest.attended_contestants.remove(user)
            user.attended_contests.remove(contest)
            return Response({'message': 'Unregister successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'You is not a contestant'}, status=status.HTTP_201_CREATED)
