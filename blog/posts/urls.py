from django.urls import path, include

from .views import PostDetail, PostList, PostCreate, UserPostRelationViewSet


from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'relations', UserPostRelationViewSet)


urlpatterns = [
    path('list/', PostList.as_view()),
    path('list/<int:pk>/', PostDetail.as_view()),
    path('create/', PostCreate.as_view()),

]
urlpatterns += router.urls
