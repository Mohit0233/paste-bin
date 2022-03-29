"""
ASGI config for PasteBin project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

#
# setup for websockets
# application = ProtocolTypeRouter({
#     "http": AsgiHandler(),
#     # IMPORTANT::Just HTTP for now. (We can add other protocols later.)
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             paste.routing.channel_routing
#         )
#     ),
# })


import os

from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from paste.routing import channel_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PasteBin.settings')

# setup for websockets
application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            channel_routing
        )
    ),
})