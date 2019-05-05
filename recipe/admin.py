from django.contrib import admin

from recipe.models import Recipe


class IngredientInlineAdmin(admin.TabularInline):
    model = Recipe.ingredients.through


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'recipe')
    search_fields = ['name']
    fieldsets = (
        (Recipe, {
            'fields': [
                ('name', 'recipe', 'meal'),
            ]
        }),
    )
    inlines = (IngredientInlineAdmin,)
