from django.urls import path, include

from .views import (
    PostDetail,
    PostCreate,
    UserPostRelationViewSet,
    PostListView, CustomPostViewSet,

)


from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'relations', UserPostRelationViewSet)

app_name = 'posts'
v = 'api/v1/'
urlpatterns = [
    path(f'{v}list/', PostListView.as_view(), name='list'),
    path(f'{v}list/<int:pk>/', PostDetail.as_view()),
    path(f'{v}create/', PostCreate.as_view()),
    path(f'{v}custom/', CustomPostViewSet.as_view()),


]
urlpatterns += router.urls
