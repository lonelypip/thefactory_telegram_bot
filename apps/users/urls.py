from django.urls import path
from .views import UserCreateAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user_create_url'),
    path('token-auth/', obtain_auth_token, name='token_auth_url')
]
