from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Todo
from .permissions import IsOwner
from .serializers import TodoSerializer


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAdminUser, )

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwner, IsAdminUser, )
