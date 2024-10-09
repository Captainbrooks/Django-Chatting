from django.urls import re_path
from .consumers import MyMessage 

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<username>[^/]+)/(?P<other_username>[^/]+)/$', MyMessage.as_asgi()),
]
