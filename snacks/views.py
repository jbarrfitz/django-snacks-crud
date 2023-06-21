from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack


class SnacksListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = "snacks"


class SnacksDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class SnacksCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = "__all__"

class SnacksUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = "__all__"


class SnacksDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")