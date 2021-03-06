from django.db import models
from django.utils import timezone

from ingredient.models import Ingredient
from meal_app.models import Meal


class Recipe(models.Model):
    name = models.CharField(max_length=30, unique=True)
    recipe = models.CharField(max_length=500)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date_field = models.DateField(default=timezone.now)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, unique=False)
    ingredient = models.ForeignKey(Ingredient, db_column='ingredient_id', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=200)
