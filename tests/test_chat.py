from django.test.testcases import TestCase
from chat.models import Message
from django.contrib.auth import get_user_model


class TestChat(TestCase):
    def test_send_message(self):
        author = get_user_model().objects.create(**{
            'email': 'qwerty@test.com',
            'password': 'QWErty1'
        }).save()

        message = Message.objects.create(**{
            'text': 'qwe',
            'author': author
        })

        self.assertIsInstance(message, Message)

