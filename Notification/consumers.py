from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json



class MyMessage(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        
        self.username=self.scope['url_route']['kwargs']['username']
        self.other_username=self.scope['url_route']['kwargs']['other_username']
        
        # sorting the names by alphabetically such that whatever the names are in, it make sure that there is a single room for both of them.
        room_members = sorted([self.username, self.other_username])
        self.room_name = f"chat_{room_members[0]}_{room_members[1]}"
        self.room_group_name = f"chat_{self.room_name}"
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        
        await self.send_json({'msg':'Welcome to the chat'})
        
    
    async def receive(self,text_data):
        
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        sender=text_data_json['username']
        receiver=text_data_json['other_username']
        
        
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':sender,
                'other_username':receiver
                
            }
        )
        
        
    
    async def chat_message(self, event):
        message=event['message']
        username=event['username']
        other_username=event['other_username']
        
        
        
        await self.send(
            text_data=json.dumps({
            'message':message,
            'username':username,
            'other_username':other_username
            
        }))
        
        
        
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
        
        
    
        
        
        
