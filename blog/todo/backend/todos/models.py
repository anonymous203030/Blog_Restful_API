from django.conf import settings
from django.db import models

from users.models import User


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)



    def __str__(self):
        return self.title
