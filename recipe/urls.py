from django.urls import path

from recipe.views import (
    recipe_create_view,
    recipe_delete_view,
    recipe_detail,
    recipe_list_view,
    recipe_update_view)

app_name = "recipe"
urlpatterns = (
    path(f'{app_name}/', view=recipe_list_view, name='list'),
    path(f'{app_name}/<str:name>/', view=recipe_detail, name='detail'),
    path(f'create/', view=recipe_create_view, name='create'),
    path(f'{app_name}/delete/<int:pk>', view=recipe_delete_view, name='delete'),
    path(f'{app_name}/update/<int:pk>', view=recipe_update_view, name='update'),
)
