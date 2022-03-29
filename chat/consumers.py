from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PrivateChat(AsyncWebsocketConsumer):
    async def connect(self):
        # room 用 id1_id2 来命名
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(self.room_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name);

    async def group_send_event(self, data):
        await self.send(text_data=json.dumps(data))

    async def send_message(self, data):
        await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': "group_send_event",
                    'event': "send_message",
                    'sid': data['sid'],
                    'rid': data['rid'],
                    'text': data['text'],
                })

    async def receive(self, text_data):
        data = json.loads(text_data)
        event = data['event']
        if event == "send_message":
            await self.send_message(data)
