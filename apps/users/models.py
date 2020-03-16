from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token_for_bot = models.CharField(max_length=300, blank=True, null=True)
    chat_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

