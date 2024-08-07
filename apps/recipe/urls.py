from django.urls import path

from apps.recipe.views import recipe


urlpatterns = [
    path('recipe/', recipe, name='recipe'),
]
