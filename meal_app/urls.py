from django.urls import path

from meal_app.views import (
    meal_create_view,
    meal_delete_view,
    meal_detail,
    meal_list_view,
    meal_update_view)

app_name = "meals"
urlpatterns = (
    path(f'{app_name}/', view=meal_list_view, name='list'),
    path(f'{app_name}/<str:name>/', view=meal_detail, name='detail'),
    path(f'create/', view=meal_create_view, name='create'),
    path(f'{app_name}/delete/<int:pk>', view=meal_delete_view, name='delete'),
    path(f'{app_name}/update/<int:pk>', view=meal_update_view, name='update'),



)

