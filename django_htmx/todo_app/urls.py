from django.urls import path

from . import views


urlpatterns = [
   path("", views.ToDoListPage.as_view(), name="page_todo_list"),
   path("", views.AddTodoPartial.as_view(), name="partial_add_todo")
]