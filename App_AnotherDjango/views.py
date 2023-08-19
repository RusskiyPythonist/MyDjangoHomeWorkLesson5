from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvForm
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
# Create your views here.


def index(request: WSGIRequest):
    advertisements: list[Advertisement] = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'advertisment/index.html', context)


def top_sellers(request: WSGIRequest):
    return render(request, 'advertisment/top-sellers.html')


def advertisement_post(request: WSGIRequest):
    if request.method == 'POST':
        form = AdvForm(request.POST, request.FILES)  # передаю все данные в форму для проверки
        if form.is_valid():  # проверяю на правильность
            adv = Advertisement(**form.cleaned_data)  # передаю данные в модель
            adv.user = request.user  # добавил в запись юзера который сделал запрос
            adv.save()  # сохранил запись в бд
            return redirect(
                reverse('main-page')
            )
    else:
        form = AdvForm()

    context = {'form': form}
    return render(request, 'advertisment/advertisement-post.html', context)


def register(request: WSGIRequest):
    return render(request, 'auth/register.html')


def login(request: WSGIRequest):
    return render(request, 'auth/login.html')


def profile(request: WSGIRequest):
    return render(request, 'auth/profile.html')