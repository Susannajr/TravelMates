from django.shortcuts import render, redirect  # ОБЯЗАТЕЛЬНО добавьте этот импорт
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm  # Исправлено название формы
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages

# Получаем кастомную модель пользователя
User = get_user_model()

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Ищем пользователя по email
            try:
                user = User.objects.get(email=cd['email'])  # Исправлено на 'email'
            except User.DoesNotExist:
                user = None

            # Проверяем пароль
            if user is not None and user.check_password(cd['password']):
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Verification is completed successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но не сохраняем сразу
            new_user = user_form.save(commit=False)
            # Устанавливаем пароль пользователя
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем пользователя
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})
@login_required
def edit(request):
    # Если у пользователя нет профиля, создаем его
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('dashboard')  # Переадресация на страницу dashboard после успешного обновления
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})