
from django.urls import path


from .views import RegisterViewSet, LoginAPiViewSet, UsersListViewSet, UserProfileListViewSet, \
    UserProfileCreateViewSet, UserProfileDetailViewSet
from rest_framework.routers import DefaultRouter

p = 'profile'
urlpatterns = [
        #USER
    path('register/',RegisterViewSet.as_view(), name='register' ),
    path('login/', LoginAPiViewSet.as_view(), name='login'),
    path('list/', UsersListViewSet.as_view(), name='list'),
        #PROFILE
    path(f'{p}/create/', UserProfileCreateViewSet.as_view(), name='create_profile'),
    path(f'{p}/list/', UserProfileListViewSet.as_view(), name='list_profile'),
    path(f'{p}/detail/<int:pk>/', UserProfileDetailViewSet.as_view(), name='change_profile'),



]
