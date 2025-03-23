from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('message', 'image_url', 'created_at') 
    search_fields = ('message',)# 
    list_filter = ('created_at',)  