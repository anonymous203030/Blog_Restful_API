from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Post, UserPostRelation
from .serializers import PostSerializer, UserPostRelationSerializer
from .permissions import IsOwner


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner, )

class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()

class UserPostRelationViewSet(viewsets.ModelViewSet):
    queryset = UserPostRelation.objects.all()
    serializer_class = UserPostRelationSerializer
    permission_classes = [IsAuthenticated]
