import uuid

from django.contrib.auth import get_user_model
from django.db import models


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_created=True)
    text = models.TextField(max_length=1024)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.author.username:.20} : {self.text:.100}{'...' if len(self.text) > 100 else ''}"
