from channels.consumer import SyncConsumer, AsyncConsumer
from channels.generic.http import AsyncHttpConsumer

from .serializers.contestant_serializers import UserContestRankSerializer
from rest_framework.settings import api_settings
from rest_framework.request import Request
from rest_framework.response import Response
from django.http.request import HttpRequest, QueryDict
from api.models import Result
from .serializers.result_serializer import UserResultWSSerializer
import json
from asyncio.tasks import sleep
import asyncio


class UserResultWebsocket(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })
        await self.handle(event)
    
    async def websocket_disconnect(self, event):
        self.close()

    
    async def handle(self, event):
        result_id = self.scope['url_route']['kwargs']['result_id']
        print('hello')
        loop = asyncio.get_running_loop()
        end_time = loop.time() + 30.0
        while True:
            await self.send_result(result_id)
            if (loop.time() + 1.0) > end_time:
                break
            await sleep(5)
        
        self.close()


    async def send_result(self, result_id):
        result_json = await self.get_result_json(result_id)
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(result_json, ensure_ascii=False)
        })        

    async def get_result_json(self, result_id):
        result = Result.objects.get(pk=result_id)
        serializer = UserResultWSSerializer(result)
        return serializer.data
