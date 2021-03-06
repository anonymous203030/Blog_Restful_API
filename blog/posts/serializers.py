from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import Posts, UserPostRelation, PostImages


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    saves_count = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ('id', 'title', 'content', 'owner', 'created_at', 'updated_at',
                  'likes_count', 'saves_count',)

    def get_likes_count(self, instance):
        return UserPostRelation.objects.filter(post=instance, like=True).count()

    def get_saves_count(self, instance):
        return UserPostRelation.objects.filter(post=instance, saved=True).count()


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ('id', 'images', 'post',)


class UserPostRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostRelation
        fields = ('id', 'user', 'post', 'like', 'saved', 'rating', 'reacted_at',)
