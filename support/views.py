from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Category, Message, UserMessage
from .forms import MessageForm, LoginForm, MessListForm


def index(request):
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                form = form.save(commit=False)
                form.user = request.user
                form.save()
        else:
            print('Error')
            return redirect('/')
    form = MessageForm()
    return render(request, "support/index.html", {'form': form})


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'registration/signup.html'


def list_message(request):
    message = request.user.messages.all()
    return render(request, 'support/message_list.html', {'message': message})


def user_message(request, pk):
    if request.method == 'POST':
        form = MessListForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                form = form.save(commit=False)
                form.user = request.user
                form.save()
        else:
            return redirect('/')
    form = MessListForm()
    messages = UserMessage.objects.filter(subject_id=pk, subject__user=request.user)
    return render(request, 'support/user_message.html', {'messages': messages, 'form': form})

# - Реализовать форму для отправки сообщения в указанный subject.
# - Реализовать вывод сообщения от модератора.
# - В итоге нужно вывести от кого и текст сообщения с каждой стороны.