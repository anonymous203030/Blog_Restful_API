from django.urls import path, include

from .views import *


# from rest_framework.routers import SimpleRouter
#
# router = SimpleRouter()
# router.register(r'relations', UserPostRelationViewSet)

app_name = 'posts'

urlpatterns = [
    # POST
    path(f'list/', PostListView.as_view(), name='list'),
    path(f'detail/<int:pk>/', PostDetail.as_view()),
    path(f'create/', PostCreate.as_view()),
    path(f'custom/', CustomPostViewSet.as_view()),

    # USER IMAGES
    path('images/create/', PostImagesCreate.as_view()),
    path('images/list/', PostImageList.as_view()),
    path('images/detail/<int:pk>/', PostImageDetail.as_view()),

    # USER POST RELATION (LIKE, SAVE)
    path(f'relation/create/', UserPostRelationCreate.as_view()),
    path(f'relation/list/', UserPostRelationList.as_view()),
    path(f'relation/detail/<int:pk>/', UserPostRelationDetail.as_view()),
    path(f'relation/custom/list/', CustomPostRelationList.as_view()),


]