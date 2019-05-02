from django.contrib import admin

from recipe.models import Recipe, Ingredient


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


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories')
    search_fields = ['name']
    fieldsets = (
        (Ingredient, {
            'fields': [
                ('name', 'calories'),
            ]
        }),
    )


