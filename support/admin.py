
from django.contrib import admin
from django.http import request

from .models import Category, Message, UserMessage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class UserMessageInline(admin.StackedInline):
    model = UserMessage
    extra = 1
    readonly_fields = ['user',]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'text', 'image', 'create_at', 'status', 'user')
    inlines = [UserMessageInline]


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'text', 'user')

