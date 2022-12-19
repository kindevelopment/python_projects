from django.urls import path

from support.views import index, list_message, user_message

urlpatterns = [
    path('message/', list_message, name='message'),
    path('usermess/<int:pk>/', user_message, name='user_message'),
    path('', index, name='main'),
]
