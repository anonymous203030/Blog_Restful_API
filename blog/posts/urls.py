from django.urls import path, include

from .views import (
    PostDetail,
    PostCreate,
    UserPostRelationViewSet,
    PostListView,

)


from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'relations', UserPostRelationViewSet)

app_name = 'posts'

urlpatterns = [
    path('list/', PostListView.as_view(), name='list'),
    path('list/<int:pk>/', PostDetail.as_view()),
    path('create/', PostCreate.as_view()),

]
urlpatterns += router.urls
