from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from .models import UserPostRelation, Posts
from .serializers import PostSerializer, UserPostRelationSerializer
from .permissions import IsOwner


# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsAuthenticated, )

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner, )

class PostCreate(generics.CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()

class UserPostRelationViewSet(viewsets.ModelViewSet):
    queryset = UserPostRelation.objects.all()
    serializer_class = UserPostRelationSerializer
    permission_classes = [IsAuthenticated]

class PostListView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = PageNumberPagination
