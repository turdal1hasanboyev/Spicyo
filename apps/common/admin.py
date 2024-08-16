from django.contrib import admin

from apps.common.models import SubEmail


@admin.register(SubEmail)
class SubEmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_email', 'created_at')
