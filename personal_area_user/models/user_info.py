from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

# Дефолтная фотография для аватарок пользователей
DEFAULT_IMAGE_PATH = "media/ava/default_images/undefined_user.jpg"


def validate_phone_number(value: str) -> None:
    """Валидатор для поля phone_number модели UserInfo."""

    if not value.isdigit():
        raise ValidationError(
            _("Номер телефона должен содержать только цифры."),
            code="invalid_phone_number",
        )

    if len(value) < 7:
        raise ValidationError(
            _("Номер телефона должен содержать как минимум 7 цифр."),
            code="invalid_phone_number",
        )


class UserInfo(models.Model):
    """Личная информация о пользователе."""

    user = models.OneToOneField(
        "CustomUser",
        related_name="info_user",
        on_delete=models.CASCADE,
        help_text="Связь личной информации пользователя с пользователем",
        verbose_name="Пользователь",
    )
    sex = models.CharField(
        blank=True,
        help_text="Пол пользователя",
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        help_text="Дата рождения пользователя",
    )
    address = models.TextField(
        blank=True,
        max_length=135,
        help_text="Местонахождение пользователя",
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[validate_phone_number],
        help_text="Номер телефона пользователя",
    )
    photo = models.ImageField(
        upload_to="ava/",
        default=DEFAULT_IMAGE_PATH,
        help_text="Аватарка пользователя",
    )
    bio = models.TextField(
        max_length=300,
        blank=True,
        help_text='Раздел "О себе"',
    )

    class Meta:
        """Метаданные о данной модели."""

        verbose_name = "Личная информация пользователя"
        verbose_name_plural = "Личная информация пользователей"

    def __str__(self):
        """Возвращает строковое представление объекта.

        :return Строковое преставление объекта
        """

        return self.user
