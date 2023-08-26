from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvForm
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models import Count
# Create your views here.

User = get_user_model()

def index(request: WSGIRequest):
    title = request.GET.get('query')
    if title:
        advertisements: list[Advertisement] = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements: list[Advertisement] = Advertisement.objects.all()
    context = {'advertisements': advertisements,
               'title': title,}
    return render(request, 'advertisment/index.html', context)


def top_sellers(request: WSGIRequest):
    users = User.objects.annotate(
        adv_count=Count('advertisement')
    ).order_by('-adv_count')

    context = {
        'users': users
    }
    return render(request, 'advertisment/top-sellers.html', context)


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


def advertisement_detail(request: WSGIRequest, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {
        "advertisement": advertisement
    }
    return render(request, 'advertisment/advertisement.html', context)


def register(request: WSGIRequest):
    return render(request, 'auth/register.html')


def login(request: WSGIRequest):
    return render(request, 'auth/login.html')


def profile(request: WSGIRequest):
    return render(request, 'auth/profile.html')