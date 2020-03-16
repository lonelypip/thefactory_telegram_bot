from rest_framework import serializers
from ..users.models import Message




class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('user', 'text',)