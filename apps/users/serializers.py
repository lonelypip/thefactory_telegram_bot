from rest_framework import serializers
from rest_framework.validators import ValidationError, UniqueValidator
from django.contrib.auth.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        label='Email',
        validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(
        required=True,
        label='First Name')
    password = serializers.CharField(label='Password', min_length=8, write_only=True)
    password2 = serializers.CharField(label='Confirm Password', write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password', 'password2')

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        email = validated_data['email']
        password = validated_data['password']
        user = User(username=username, email=email, first_name=first_name)

        if password != validated_data['password2']:
            raise ValidationError('Passwords not match!')
        else:
            user.set_password(password)
            user.save()
        return validated_data


