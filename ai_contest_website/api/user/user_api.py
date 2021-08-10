from rest_framework.response import Response
from rest_framework import generics
from .serializers.contestant_serializers import UserListRegisterContestsSerializer
from api.models import User
from api.user.serializers.contest_serializers import UserContestInfoSerializer
from api.models.Contest import Contestant
from api.utils import time_utils


class UserListRegisterContests(generics.GenericAPIView):

    def get_contest(self, list_contest, contest_status: str):
        new_contests = []
        for attended_contest in list_contest:
            time_start = attended_contest.contest.time_start
            time_end = attended_contest.contest.time_end
            if time_utils.get_status_contest(time_start, time_end) == contest_status:
                new_contests.append(attended_contest)
        return new_contests

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('user_id')
        # TODO: change this to user'attended_contests
        attended_contests = list(Contestant.objects.filter(user_id=id).order_by('-_id'))
        print(request.GET.get('status'))
        if request.GET.get('status') is not None:
            data = self.get_contest(attended_contests, request.GET.get('status'))
        else:
            data = attended_contests
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = UserListRegisterContestsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = UserListRegisterContestsSerializer(attended_contests, many=True)
        return Response(serializer.data)