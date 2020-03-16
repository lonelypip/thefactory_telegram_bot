from django.urls import path
from .views import BotConnectionAPIView, ChatUpdateAPIView, SendMessageAPIView


urlpatterns = [
    path('connection/', BotConnectionAPIView.as_view(), name='bot_connection_url'),
    path('update/', ChatUpdateAPIView.as_view(), name='chat_update_url'),
    path('send-message/', SendMessageAPIView.as_view(), name='send_message_url')
]
