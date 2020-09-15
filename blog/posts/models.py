from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='my_posts')

    who_liked = models.ManyToManyField(User, through='UserPostRelation'
                                       ,related_name='liked')
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

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    reacted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Owner{self.user.username} ,Post:{Post.title}, Rating:{self.rating}'