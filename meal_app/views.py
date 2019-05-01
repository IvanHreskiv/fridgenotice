from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from meal_app.models import Meal


class MealListView(LoginRequiredMixin, ListView):

    model = Meal
    slug_field = "name"
    slug_url_kwarg = "name"


meal_list_view = MealListView.as_view()


class MealDetailView(LoginRequiredMixin, DetailView):

    model = Meal
    slug_field = "name"
    slug_url_kwarg = "name"


meal_detail = MealDetailView.as_view()


class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = reverse_lazy('meals:list')


meal_delete_view = MealDeleteView.as_view()


class MealCreateView(LoginRequiredMixin, CreateView):

    fields = ['name', 'detail']
    model = Meal
    success_url = reverse_lazy('meals:list')


meal_create_view = MealCreateView.as_view()


class MealUpdateView(LoginRequiredMixin, UpdateView):

    model = Meal
    fields = ['name', 'detail']
    success_url = reverse_lazy('meals:list')


meal_update_view = MealUpdateView.as_view()
