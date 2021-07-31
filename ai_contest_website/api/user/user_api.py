from rest_framework.response import Response
from rest_framework import generics
from .serializers.contestant_serializers import UserListAttendedContestsSerializer
from api.models import User
from api.user.serializers.contest_serializers import UserContestInfoSerializer
from api.models.Contest import Contestant


class UserListAttendedContests(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('user_id')
        attended_contests = list(Contestant.objects.filter(user_id=id))
        page = self.paginate_queryset(attended_contests)
        if page is not None:
            serializer = UserListAttendedContestsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = UserListAttendedContestsSerializer(attended_contests, many=True)
        return Response(serializer.data)
        