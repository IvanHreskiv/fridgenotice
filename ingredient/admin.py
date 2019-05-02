from django.contrib import admin

from ingredient.models import Ingredient


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
