from rest_framework.response import Response
from rest_framework import status, generics
from api.models import Contest
from api.models.Contest import Contestant
from .serializers.contestant_serializers import UserContestRankSerializer

class UserContestRank(generics.GenericAPIView):
    """Represent final ranking of a contest"""
    def get(self, request, *args, **kwargs):
        """
        Return final ranking of a contest with sort order
        """
        try:
            contest_id = kwargs.get('contest_id')
            if contest_id is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            # Descending total score of list
            rank_list = Contestant.objects.filter(contest_id=contest_id).order_by('-total_score')
            serializer = UserContestRankSerializer(rank_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
