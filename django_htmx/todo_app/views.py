from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from todo_app.forms import TodoForm
from todo_app.models import TodoItem


class ToDoListPage(ListView):
    model = TodoItem
    template_name = "todo_list.html"
    context_object_name = "todo_items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TodoForm()

        return context


class AddTodoPartial(View):
    def post(self, request, party_uuid, *args, **kwargs):
        form = TodoForm(request.POST)
        if form.is_valid():
            gift = form.save()

            return render(request, "party/gift_registry/partial_gift_detail.html", {"gift": gift, "party": party})
