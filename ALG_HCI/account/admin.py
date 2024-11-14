from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Profile

# Получаем вашу кастомную модель пользователя
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        'email', 'first_name', 'last_name', 'is_staff', 
        'is_active', 'date_of_birth', 'photo', 'phone_number'  # Добавляем phone_number
    ]
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email', 'first_name', 'last_name', 'phone_number']  # Добавляем phone_number в поиск
    ordering = ['email']

    # Поля, которые будут отображаться в форме пользователя
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),  # Добавляем phone_number
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('date_joined',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff'),  # Добавляем phone_number
        }),
    )

    # Указываем поле date_joined как только для чтения
    readonly_fields = ('date_joined',)

# Регистрируем модель CustomUser с ее конфигурацией
admin.site.register(CustomUser, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'date_of_birth', 'photo')
    search_fields = ('user__email',)
    list_filter = ('date_of_birth',)
    ordering = ('user',)

# Регистрируем модель Profile в админке
admin.site.register(Profile, ProfileAdmin)
