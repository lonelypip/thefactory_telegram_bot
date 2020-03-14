from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from random import choice
from string import ascii_letters
from apps.users.models import Profile
from .functions import extract_token_code

import json

class BotConnectionAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user

        if Profile.objects.filter(user=user).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'BOT': 'You are already connected to the bot'})

        token_for_bot = ''.join(choice(ascii_letters) for i in range(15))
        Profile.objects.create(user=user, token_for_bot=token_for_bot)

        return Response(status=status.HTTP_201_CREATED, data={
            'OK': 'True',
            'URL': f'https://telegram.me/thefact_bot?start={token_for_bot}'
        })


class ChatUpdateAPIView(APIView):
    def post(self, request):
        r = request.data
        token = extract_token_code(r['message']['text'])
        if token:
            chat_id = r['message']['chat']['id']
            print(chat_id)
            return Response(data=r)

