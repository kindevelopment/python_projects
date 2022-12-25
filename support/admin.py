
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.forms import BaseInlineFormSet
from django.http import request

from .forms import MessListForm
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
    list_filter = ('create_at', 'status', 'category')
    search_fields = ('user__username', )

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'text', 'user')

