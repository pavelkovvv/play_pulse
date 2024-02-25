from django.core.validators import MaxValueValidator
from django.db import models

from game.models import Game
from personal_area_user.models import CustomUser


class GameUser(models.Model):
    """Игра пользователя."""

    user = models.ForeignKey(
        CustomUser,
        related_name="user_gameuser",
        on_delete=models.CASCADE,
        help_text="Связь игры пользователя с пользователем",
        verbose_name="Пользователь",
    )
    game = models.ForeignKey(
        Game,
        related_name="game_gameuser",
        on_delete=models.CASCADE,
        help_text="Связь игры пользователя с игрой",
        verbose_name="Игра",
    )
    completion_date = models.DateField(
        blank=True,
        help_text="Дата прохождения игры пользователем",
        verbose_name="Дата прохождения игры",
    )
    rating = models.PositiveIntegerField(
        blank=True,
        validators=[MaxValueValidator(10)],
        help_text="Рейтинг игры пользователем",
        verbose_name="Рейтинг игры",
    )
    start_date = models.DateField(
        blank=True,
        help_text="Дата начала прохождения игры пользователем",
        verbose_name="Дата начала прохождения игры",
    )
    end_date = models.DateField(
        blank=True,
        help_text="Дата завершения прохождения игры пользователем",
        verbose_name="Дата завершения прохождения игры",
    )
    progress = models.PositiveIntegerField(
        blank=True,
        validators=[MaxValueValidator(100)],
        help_text="Прогресс прохождения игры (в процентах)",
        verbose_name="Прогресс прохождения игры",
    )

    class Meta:
        """Метаданные данной модели."""

        verbose_name = "Игра пользователя"
        verbose_name_plural = "Набор игр пользователей"

    def __str__(self):
        """Возвращает строковое представление объекта.

        :return Строковое преставление объекта
        """

        return f"Игра {self.game} пользователя {self.user}"
