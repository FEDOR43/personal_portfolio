from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    list_display = ('title', 'published', 'blog_text')
