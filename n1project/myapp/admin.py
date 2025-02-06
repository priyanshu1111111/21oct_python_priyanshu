

# Register your models here.
from django.contrib import admin
from .models import Snippet, Comment

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'created_at')
    search_fields = ('title', 'owner__username')
    list_filter = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'snippet', 'author', 'created_at')
    search_fields = ('snippet__title', 'author__username')
    list_filter = ('created_at',)
