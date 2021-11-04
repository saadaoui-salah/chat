from django.urls import re_path 
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    # re_path(r'peer[12]/', consumers.ChatConsumer.as_asgi()),
    # re_path(r"", consumers.ChatConsumer.as_asgi()),
    # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    # url(r'tmpy/', consumers.ChatConsumer.as_asgi()), 
    url(r'^ws/play/(?P<roomid>\w+)/$', consumers.ChatConsumer.as_asgi()), 
]  