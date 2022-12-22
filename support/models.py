from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Message(models.Model):
    subject = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='messages')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class UserMessage(models.Model):
    text = models.TextField()
    subject = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='messages_list')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.get_username()

    class Meta:
        verbose_name = 'Сообщение от пользователя'
        verbose_name_plural = 'Сообщения от пользователей'