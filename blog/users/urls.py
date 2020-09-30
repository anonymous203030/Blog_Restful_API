
from django.urls import path


from .views import RegisterViewSet, LoginAPiViewSet, UsersListViewSet, UserProfileListViewSet, \
    UserProfileCreateViewSet, UserProfileDetailViewSet
from rest_framework.routers import DefaultRouter

p = 'profile/'
v = 'api/v1/'
urlpatterns = [
        #USER
    path(f'{v}register/',RegisterViewSet.as_view(), name='register' ),
    path(f'{v}login/', LoginAPiViewSet.as_view(), name='login'),
    path(f'{v}list/', UsersListViewSet.as_view(), name='list'),
        #PROFILE
    path(f'{v}{p}create/', UserProfileCreateViewSet.as_view(), name='create_profile'),
    path(f'{v}{p}list/', UserProfileListViewSet.as_view(), name='list_profile'),
    path(f'{v}{p}detail/<int:pk>/', UserProfileDetailViewSet.as_view(), name='change_profile'),



]
