from django.db import models

from game.models.game import Game
from personal_area_user.models import CustomUser


class Comment(models.Model):
    """Модель комментария."""

    user = models.ForeignKey(
        CustomUser,
        related_name="comment_user",
        on_delete=models.PROTECT,
        help_text="Связь комментария с пользователем",
        verbose_name="Пользователь",
    )
    game = models.ForeignKey(
        Game,
        related_name="comment_game",
        on_delete=models.PROTECT,
        help_text="Связь комментария с игрой",
        verbose_name="Игра",
    )
    comment_text = models.TextField(
        help_text="Текст комментария",
        verbose_name="Комментарий",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        """Метаданные о данной модели."""

        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        """Возвращает строковое представление объекта.

        :return Строковое преставление объекта
        """

        return f"{self.game} - {self.user}"
