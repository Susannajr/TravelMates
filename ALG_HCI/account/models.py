from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

# Менеджер для кастомной модели пользователя
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

# Кастомная модель пользователя
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # Уникальный email
    first_name = models.CharField(max_length=30)  # Имя
    last_name = models.CharField(max_length=30)  # Фамилия
    is_active = models.BooleanField(default=True)  # Активен ли пользователь
    is_staff = models.BooleanField(default=False)  # Является ли сотрудником (для доступа к админке)
    date_joined = models.DateTimeField(auto_now_add=True)  # Дата регистрации
    bio = models.TextField(default="No bio provided")
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Добавлено поле phone_number

    # Поля для работы с группами и разрешениями
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_set", blank=True)

    objects = CustomUserManager()  # Использование кастомного менеджера

    USERNAME_FIELD = 'email'  # Использовать email для входа
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Обязательные поля при создании пользователя

    def __str__(self):
        return self.email

#Модель профиля пользователя
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)





    def __str__(self):
        return self.user.email  # Используйте `email`, так как `username` может отсутствовать

