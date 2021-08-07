"""
ASGI config for ai_contest_website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
import api.user


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_contest_website.server.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            api.user.urls.ws_urlpatterns
        )
    )
})