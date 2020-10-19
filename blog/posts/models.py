from django.db import models

from users.models import User


class Posts(models.Model):
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

    class Meta:
        app_label = 'd61nc0nbgsq65g'

class PostImages(models.Model):
    images = models.ImageField(upload_to='post_image/')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    class Meta:
        app_label = 'd61nc0nbgsq65g'

    def __str__(self):
        return f'Post:{self.post} | Images: {self.images}'


class UserPostRelation(models.Model):
    RATE_CHOICES = (
        (1,'*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.OneToOneField(Posts, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    reacted_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'd61nc0nbgsq65g'

    def __str__(self):
        return f'Owner{self.user}, Post:{Posts.title}, Rating:{self.rating}'
