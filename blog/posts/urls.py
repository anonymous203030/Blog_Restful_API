from django.urls import path

from .views import PostDetail, PostList, PostCreate

urlpatterns = [
    path('list/', PostList.as_view()),
    path('list/<int:pk>/', PostDetail.as_view()),
    path('create/', PostCreate.as_view()),

]