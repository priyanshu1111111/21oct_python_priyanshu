from django.contrib import admin
from .models import post_tbl

class Data(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at']

admin.site.register(post_tbl, Data)
