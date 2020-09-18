from django.db import models

from users.models import User


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

