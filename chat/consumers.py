import json
from channels.generic.websocket import AsyncWebsocketConsumer
import django
django.setup()
from .models import Message
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    default_room = '0'

    async def connect(self):
        await self.channel_layer.group_add(
            self.default_room,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.default_room,
            self.channel_layer
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        text = text_data_json["message"]
        email = text_data_json["email"]
        author = get_user_model().objects.aget(email=email)
        message = Message.objects.acreate(
            author=await author,
            text=text
        )
        message = await message
        await sync_to_async(message.save)()
        await self.channel_layer.group_send(
            self.default_room, {
                "type": "send_message",
                "message": text,
                "email": email,
            })

    async def send_message(self, event):
        message = event["message"]
        email = event["email"]
        await self.send(text_data=json.dumps({"message": message, "email": email}))