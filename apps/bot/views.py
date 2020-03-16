from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from random import choice
from string import ascii_letters
from apps.users.models import Profile
from .functions import extract_token_code, send_message_telegram
from . serializers import SendMessageSerializer
from ..users.models import Message




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
        chat_id = r['message']['chat']['id']

        if token:
            if Profile.objects.filter(token_for_bot=str(token)).exists():
                profile = Profile.objects.get(token_for_bot=token)
                profile.chat_id = chat_id
                profile.save()
                send_message_telegram(chat_id, text='Welcome!')
                return Response(data=r)
            else:
                send_message_telegram(chat_id, text="I don't know who you are!")
                return Response(data=r)

        send_message_telegram(
            chat_id,
            text='Please start from this website '
                 'https://factoryproject.herokuapp.com/users/token-auth/ '
                  'Website'
        )
        return Response(data=r)


class SendMessageAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = SendMessageSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if request.data.get('text'):
            text = request.data['text']
            print(request.user.first_name)
            send_message_telegram(
                request.user.profile.chat_id,
                text=
                f'{request.user.first_name}, я получил от тебя сообщение: {text}'
            )
            message = Message.objects.create(user=request.user,
                                             text=text)
            serializer = SendMessageSerializer(message, context={'request': request})
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'BOT': 'Text field is required!'})

