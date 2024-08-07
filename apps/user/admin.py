from django.contrib import admin

from apps.user.models import User, About


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'created_at')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    