from rest_framework import generics

from todo.api.serializers import TodoItemSerializer
from todo.models import TodoItem


class ToDoListViewSet(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
