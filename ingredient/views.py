from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from ingredient.models import Ingredient


class IngredientListView(LoginRequiredMixin, ListView):

    model = Ingredient
    slug_field = "name"
    slug_url_kwarg = "name"


ingredient_list_view = IngredientListView.as_view()


class IngredientDetailView(LoginRequiredMixin, DetailView):

    model = Ingredient
    slug_field = "name"
    slug_url_kwarg = "name"


ingredient_detail = IngredientDetailView.as_view()


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = reverse_lazy('ingredients:list')


ingredient_delete_view = IngredientDeleteView.as_view()


class IngredientCreateView(LoginRequiredMixin, CreateView):

    fields = ['name', 'calories']
    model = Ingredient
    success_url = reverse_lazy('ingredients:list')


ingredient_create_view = IngredientCreateView.as_view()


class IngredientUpdateView(LoginRequiredMixin, UpdateView):

    model = Ingredient
    fields = ['name', 'calories']
    success_url = reverse_lazy('ingredients:list')


ingredient_update_view = IngredientUpdateView.as_view()
