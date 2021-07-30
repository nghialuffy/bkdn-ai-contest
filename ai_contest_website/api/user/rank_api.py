

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.models import Contest

class UserContestRank(APIView):
    """Represent final ranking of a contest"""
    def get(self, request, *args, **kwargs):
        """
        Return final ranking of a contest
        """
        try:
            contest_id = kwargs.get('contest_id')
            if contest_id is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            contest = Contest.objects.get(id=contest_id)
            if contest is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            rank = contest.get_rank()
            return Response(rank, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)