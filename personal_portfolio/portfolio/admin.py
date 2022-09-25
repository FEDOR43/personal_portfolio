from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    list_display = ('title', 'description', 'image', 'url')
