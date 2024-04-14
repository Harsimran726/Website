from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(query)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']

admin.site.register(ChatConversation)

class history(admin.ModelAdmin):
    list_display = ('user_id', 'bot_message', 'user_message', 'timestamp')
    list_filter = ("timestamp",)
    search_fields = ['user_id', 'bot_message', 'user_message']
admin.site.register(Post, PostAdmin)