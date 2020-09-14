
from django.urls import path


from .views import RegisterView, LoginAPiView

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register' ),
    path('login/', LoginAPiView.as_view(), name='login'),
]