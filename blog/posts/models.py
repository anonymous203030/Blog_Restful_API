from django.conf import settings
from django.db import models

from users.models import User


class Posts(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')

    who_liked = models.ManyToManyField(User, through='UserPostRelation', related_name='liked_post')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class PostImages(models.Model):
    images = models.ImageField(upload_to='post_image/')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='post_image')

    def __str__(self):
        return f'Post:{self.post} | Images: {self.images}'


class UserPostRelation(models.Model):
    RATE_CHOICES = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_reacted')
    post = models.OneToOneField(Posts, on_delete=models.CASCADE, related_name='reacted_post')
    like = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    reacted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Owner{self.user}, Post:{Posts.title}, Rating:{self.rating}'
