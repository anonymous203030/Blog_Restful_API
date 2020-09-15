from rest_framework import serializers

from .models import Post, UserPostRelation


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', )
        model = Post

class UserPostRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostRelation
        fields = ('user', 'post', 'like', 'saved', 'rating', 'reacted_at',)
