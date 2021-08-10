# This class is a Websocket Consumer that is used to receive the rank of the users realtime.
# The rank is sent to the client in the form of a json object.
# The client is the one that is connected to the socket.
# The server is the one that is listening to the socket.

# Import the necessary libraries
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.generic.http import AsyncHttpConsumer

from api.models.Contest import Contestant
from api.models import Problem, Result
from api.user.rank_api import UserContestRank
from .serializers.contestant_serializers import UserContestRankSerializer
import json
from asyncio.tasks import sleep
import asyncio

from rest_framework.settings import api_settings
from rest_framework.request import Request
from rest_framework.response import Response
from django.http.request import HttpRequest, QueryDict
class UserContestRankWebsocket(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })
        contest_id = self.scope['url_route']['kwargs']['contest_id']
        if contest_id is not None:
            await self.loop_send_contest_rank(contest_id)
    
    async def websocket_disconnect(self, event):
        print("disconnected")
        self.close()

    
    async def handle(self, event):
        contest_id = self.scope['url_route']['kwargs']['contest_id']
        if contest_id is not None:
            self.loop_send_contest_rank(contest_id)

    async def loop_send_contest_rank(self, contest_id):
        loop = asyncio.get_running_loop()
        while True:
            await self.send_contest_rank(contest_id)
            await sleep(5)

    async def send_contest_rank(self, contest_id):
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(self.get_contest_rank_json(contest_id), ensure_ascii=False)
        })        

    def get_contest_rank_json(self, contest_id):

        list_problems = Problem.objects.filter(contest=contest_id)
        list_contestants = Contestant.objects.filter(contest_id=contest_id).order_by('-total_score')
        # score from problem
        # accuracy from result
        for contestant in list_contestants:
            total_score = 0
            for problem in list_problems:
                max_result = Result.objects.filter(problem = problem, created_user = contestant.user).order_by('-accuracy').first()
                if max_result and max_result.accuracy:
                    total_score += problem.score*max_result.accuracy*100
            contestant.total_score = total_score
            contestant.save()
        
        list_contestants = Contestant.objects.filter(contest_id=contest_id).order_by('-total_score')
        pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        http_request = HttpRequest()
        http_request.GET = QueryDict('limit=10')
        request = Request(http_request)
        pc = pagination_class()
        p = pc.paginate_queryset(list_contestants, request, None)
        serializer = UserContestRankSerializer(p, many=True)
        response = pc.get_paginated_response(serializer.data)
        return response.data

# contest_id = '610350929b3c82229413a7f0'
# list_problems = Problem.objects.filter(contest=contest_id)
# list_contestants = Contestant.objects.filter(contest_id=contest_id).order_by('-total_score')
# print(list_contestants.count())
# print(list_problems.count())
# # score from problem
# # accuracy from result
# for contestant in list_contestants:
#     total_score = 0
#     for problem in list_problems:
#         max_result = Result.objects.filter(problem = problem, created_user = contestant.user).order_by('-accuracy').first()
#         if max_result and max_result.accuracy:
#             total_score += problem.score*max_result.accuracy
#     contestant.total_score = total_score
#     contestant.save()