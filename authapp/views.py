from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from authapp.forms import UserRegisterForm, UserLoginForm, UserProfileForm
from django.contrib import messages
from authapp.models import User
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required

# функцияя = вьюхи = контролеры.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'GeekShop - Авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def new_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))




@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'GeekShop - Профиль',
        'baskets': Basket.objects.filter(user= request.user),}
    return render(request, 'authapp/profile.html', context)
