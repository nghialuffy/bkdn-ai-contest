from api.models import Contest
from rest_framework.response import Response
from .serializers import OrganizerContestantsInContestSerializer


# class UserContestantsInContest(GenericAPIView):
#     serializer_class = OrganizerContestantsInContestSerializer
#     # permission_classes = (IsAuthenticated, IsOrganizer)

#     def list(self, request, *args, **kwargs):
#         try:
#             contest_id = kwargs['contest_id']
#             contest = Contest.objects.get(id=contest_id)
#             users = contest.attended_contestants.all()
#             serializer = OrganizerContestantsInContestSerializer(users, many=True)
#             return Response(serializer.data)
#         except:
#             return Response({'status': 'false', 'message': 'No such contest'})