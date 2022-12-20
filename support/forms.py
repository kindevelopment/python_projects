from django import forms

from .models import Message, UserMessage


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("subject", "text", "image", "category",)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class MessListForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ('text',)