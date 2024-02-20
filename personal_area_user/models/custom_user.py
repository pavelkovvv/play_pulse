from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    """Модель с настройками пользователя."""

    username = models.CharField(
        db_index=True, max_length=40, unique=True, null=False, help_text='Ник пользователя'
    )
    first_name = models.CharField(max_length=35, blank=True, help_text='Имя пользователя')
    last_name = models.CharField(max_length=35, blank=True, help_text='Фамилия пользователя')
    email = models.EmailField(blank=True, null=False, help_text='Email пользователя')
    sex = models.CharField(blank=True, help_text='Пол пользователя')
    birth_date = models.DateField(blank=True, null=True, help_text='Дата рождения пользователя')
    location = models.CharField(
        max_length=100, blank=True, help_text='Город, в котором находится пользователь'
    )
    is_admin = models.BooleanField(
        default=False, help_text='Является ли пользователь администратором'
    )
    date_joined = models.DateTimeField(
        default=timezone.now, help_text='Дата регистрации пользователя'
    )

    def __str__(self):
        """Возвращает строковое представление объекта.

        :return Строковое преставление объекта
        """
        return self.username
