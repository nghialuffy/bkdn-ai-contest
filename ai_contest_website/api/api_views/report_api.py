import json

from rest_framework import generics, status
from rest_framework.response import Response
from api.models import User, Contest, Problem, Result, Language


class ReportApi(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        n_contests = Contest.objects.count()
        n_languages = Language.objects.count()
        n_problems = Problem.objects.count()
        n_results = Result.objects.count()
        n_users = User.objects.count()

        report = dict(
            n_contests=n_contests,
            n_languages=n_languages,
            n_problems=n_problems,
            n_results=n_results,
            n_users=n_users
        )
        print(report)
        return Response(report)
