from django.contrib import admin

from .models import Category, Message


admin.site.register(Category)
admin.site.register(Message)
