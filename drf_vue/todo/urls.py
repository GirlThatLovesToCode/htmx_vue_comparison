from django.urls import path

from . import views


urlpatterns = [
   path("", views.ToDoListViewSet.as_view(), name="todo_list"),
]