from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from .filters import IsOwnerFilter
from .models import UserPostRelation, Posts, PostImages
from .serializers import PostSerializer, UserPostRelationSerializer, PostImagesSerializer
from .permissions import IsOwner



#POST CREATION

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


class PostListView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = PageNumberPagination
    search_fields = ('title', 'content', 'rating', )
    ordering = ['created_at']


class CustomPostViewSet(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner, )
    pagination_class = PageNumberPagination
    filter_backends = (IsOwnerFilter, )
    search_fields = ('title', 'content', 'rating', )
    ordering = ['created_at']


# POST IMAGES

class PostImagesCreate(generics.CreateAPIView):
    queryset = PostImages.objects.all()
    serializer_class = PostImagesSerializer
    permission_classes = [IsAuthenticated]


class PostImageList(generics.ListAPIView):
    queryset = PostImages.objects.all()
    serializer_class = PostImagesSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    search_filters = ('post', )


class PostImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostImages.objects.all()
    serializer_class = PostImagesSerializer
    permission_classes = [IsOwner]
    pagination_class = PageNumberPagination
    search_filters = ('post', )


# USER-POST RELATION


class UserPostRelationCreate(generics.CreateAPIView):
    queryset = UserPostRelation.objects.all()
    serializer_class = UserPostRelationSerializer
    permission_classes = [IsAuthenticated]

class UserPostRelationList(generics.ListAPIView):
    queryset = UserPostRelation.objects.all()
    serializer_class = UserPostRelationSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    search_fields = ('user', 'post',)
    ordering = ['reacted_at']


class UserPostRelationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPostRelation.objects.all()
    serializer_class = UserPostRelationSerializer
    permission_classes = [IsOwner]


class CustomPostRelationList(generics.ListAPIView):
    queryset = UserPostRelation.objects.all()
    serializer_class = UserPostRelationSerializer
    permission_classes = [IsOwner]
    filter_backends = (IsOwnerFilter, )
    pagination_class = PageNumberPagination
    ordering = ['reacted_at']
