from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from recipe.models import Recipe


class RecipeListView(LoginRequiredMixin, ListView):

    model = Recipe
    slug_field = "name"
    slug_url_kwarg = "name"


recipe_list_view = RecipeListView.as_view()


class RecipeDetailView(LoginRequiredMixin, DetailView):

    model = Recipe
    slug_field = "name"
    slug_url_kwarg = "name"


recipe_detail_view = RecipeDetailView.as_view()


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:list')


recipe_delete_view = RecipeDeleteView.as_view()


class RecipeCreateView(LoginRequiredMixin, CreateView):

    fields = ['name', 'recipe']
    model = Recipe
    success_url = reverse_lazy('recipes:list')


recipe_create_view = RecipeCreateView.as_view()


class RecipeUpdateView(LoginRequiredMixin, UpdateView):

    model = Recipe
    fields = ['name', 'recipe']
    success_url = reverse_lazy('recipes:list')


recipe_update_view = RecipeUpdateView.as_view()
