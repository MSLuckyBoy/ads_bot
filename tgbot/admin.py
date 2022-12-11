from django.contrib import admin
from django.utils.safestring import mark_safe

from mptt.admin import DraggableMPTTAdmin

from .models import User, Category, Post


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'first_name', 'username', 'phone_number', 'is_admin', 'is_blocked', 'time_create')
    list_display_links = ('id', 'chat_id')
    search_fields = ('chat_id', 'first_name', 'username', 'phone_number')
    list_filter = ('is_admin', 'is_blocked', 'time_create')
    fields = ('chat_id', 'first_name', 'username', 'phone_number', 'language', 'region', ('is_admin', 'is_blocked'), 'time_create')
    readonly_fields = ('time_create',)


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 50
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'currency', 'author', 'status', 'time_create', 'time_update')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('currency', 'status', 'time_create', 'time_update')
    fields = ('title', 'description', 'price', 'currency', 'image', 'author', 'category', 'status', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update')


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)