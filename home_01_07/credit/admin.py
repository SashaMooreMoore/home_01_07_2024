from django.contrib import admin
from .models import Info

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'credit', 'percent', 'duration']
    list_display_links = ['name', 'credit', 'percent', 'duration']
