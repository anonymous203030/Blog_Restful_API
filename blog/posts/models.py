from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class UserPostRelation(models.Model):
    RATE_CHOICES = (
        (1,'*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)
    rating = models.CharField(choices=RATE_CHOICES, max_length=100)