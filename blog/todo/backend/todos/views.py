from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Todo
from .permissions import IsOwner
from .serializers import TodoSerializer


class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAdminUser, IsAuthenticated, )


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAdminUser, )

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwner, IsAdminUser, )
