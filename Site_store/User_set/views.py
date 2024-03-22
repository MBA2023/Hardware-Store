from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_2


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'Выполнен вход в систему {user}!')
                    return redirect('store-home')
                else:
                    return HttpResponse('Несуществующий аккаунт')
            else:
                return HttpResponse('Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'users_set/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаём объект нового юзера
            new_user = user_form.save(commit=False)
            # Устанавливаем пароль
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем
            new_user.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}! Теперь можно войти в систему.')
            return redirect('login')

    else:
        user_form = UserRegistrationForm()
    return render(request, 'users_set/reg.html', {'user_form': user_form})


def logout(request):
    logout_2(request)
    return render(request, 'users_set/logout.html')


@login_required
def profile(request):
    return render(request, 'users_set/profile.html')