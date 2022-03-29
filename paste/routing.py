# from channels.routing import route
# from django.conf.urls import url
from django.urls import re_path

from paste.consumers import ChatConsumer

channel_routing = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    # route('websocket.connect', ws_connect),
    # route('websocket.disconnect', ws_disconnect),
]