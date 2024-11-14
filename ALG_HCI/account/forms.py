from django import forms
from .models import CustomUser, Profile  # Импортируем кастомные модели

# Форма для входа
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)

# Форма для регистрации
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser  # Используем кастомную модель пользователя
        fields = ['first_name', 'last_name', 'email', 'phone_number']  # Включаем phone_number

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password']
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if CustomUser.objects.filter(email=data).exists():  # Используем CustomUser
            raise forms.ValidationError('Email already in use')
        return data

# Форма для редактирования пользователя
class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Используем кастомную модель пользователя
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        # Проверка уникальности email для редактирования, исключая текущего пользователя
        qs = CustomUser.objects.exclude(id=self.instance.id).filter(email=data)  # Используем CustomUser
        if qs.exists():
            raise forms.ValidationError('Email already in use')
        return data

# Форма для редактирования профиля
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'date_of_birth', 'photo']
