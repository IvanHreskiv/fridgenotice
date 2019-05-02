from django.contrib import admin

from meal_app.models import Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail')
    search_fields = ['name']
    fieldsets = (
        (Meal, {
            'fields': [
                ('name', 'detail'),
            ]
        }),
    )
