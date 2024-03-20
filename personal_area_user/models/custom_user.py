from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    """Модель с настройками пользователя."""

    username = models.CharField(
        unique=True,
        max_length=40,
        null=False,
        help_text="Ник пользователя",
        verbose_name="Ник пользователя",
    )
    email = models.EmailField(
        blank=True,
        null=False,
        help_text="Email пользователя",
        verbose_name="Почта пользователя",
    )
    is_admin = models.BooleanField(
        default=False,
        help_text="Является ли пользователь администратором",
        verbose_name="Флаг наличия прав администратора",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Онлайн пользователь или нет",
        verbose_name="Флаг наличия онлайна пользователя",
    )
    first_name = models.CharField(
        max_length=35,
        blank=True,
        help_text="Имя пользователя",
        verbose_name="Имя пользователя",
    )
    last_name = models.CharField(
        max_length=35,
        blank=True,
        help_text="Фамилия пользователя",
        verbose_name="Фамилия пользователя",
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        help_text="Дата регистрации пользователя",
        verbose_name="Дата регистрации",
    )

    class Meta:
        """Метаданные о данной модели."""

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        """Возвращает строковое представление объекта.

        :return Строковое преставление объекта
        """

        return self.username
