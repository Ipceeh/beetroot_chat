from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from .models import Message


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email']


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'date_created', 'text', 'author']
