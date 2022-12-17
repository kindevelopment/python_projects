from django.urls import path

from support.views import index, list_message

urlpatterns = [
    path('message/', list_message, name='message'),
    path('', index, name='main'),
]
