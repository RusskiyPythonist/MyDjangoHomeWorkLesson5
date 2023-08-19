from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('profile'))
        else:
            return render(request, 'auth/login.html')

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(reverse('profile'))
    else:
        return render(request, 'auth/login.html', {"error": 'Пользователь не найден'})

@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'auth/profile.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))