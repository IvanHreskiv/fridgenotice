from django.urls import path

from ingredient.views import (
    ingredient_create_view,
    ingredient_delete_view,
    ingredient_detail,
    ingredient_list_view,
    ingredient_update_view)

app_name = "ingredients"
urlpatterns = (
    path(f'{app_name}/', view=ingredient_list_view, name='list'),
    path(f'{app_name}/details/<str:name>/', view=ingredient_detail, name='detail'),
    path(f'{app_name}/create/', view=ingredient_create_view, name='create'),
    path(f'{app_name}/delete/<int:pk>', view=ingredient_delete_view, name='delete'),
    path(f'{app_name}/update/<int:pk>', view=ingredient_update_view, name='update'),
)
