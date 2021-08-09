from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from api.models.Problem import Problem
from .serializers.problem_serializers import UserProblemOnContestIdSerializer

class UserProblemsOnContestId(generics.ListAPIView):
    serializer_class = UserProblemOnContestIdSerializer

    def get(self, request, *args, **kwargs):
        contest_id = self.request.GET.get('contest_id')
        print(contest_id)
        problems = Problem.objects.filter(contest_id=contest_id)
        print(problems)
        serializer = self.serializer_class(problems, many=True)
        return Response(serializer.data)

