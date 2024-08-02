from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/publish/', consumers.PublishConsumer.as_asgi()),
    path('ws/subscribe/', consumers.SubscribeConsumer.as_asgi()),
]
