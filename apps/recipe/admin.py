from django.contrib import admin

from apps.recipe.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "created_at")
