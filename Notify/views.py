from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from channels.layers import get_channel_layer
import json

# Create your views here.



def index(request):
    return render(request,"index.html")




async def send(request):  
    
    if request.method=="POST":
        data=request.POST
        
        
        
        
        message=data.get('message').lower()
        
        if message=="hi from milton":
            reply='hi from server'
            channel_layer=get_channel_layer()
            await (channel_layer.group_send)(
            'my_message_group',
            {
                'type':'sendMessage',
                'msg':json.dumps(reply)
            }
        )
        print(message)
        
        
        
    return redirect('/')





def chat_room(request, username, other_username):
    print(username,other_username)
    return render(request, 'chat.html', {'username': username, 'other_username': other_username})
    



