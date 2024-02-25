from django.db import models
from django.utils import timezone

from game.models import Game


class News(models.Model):
    """Новости по игре."""

    game = models.ForeignKey(
        Game,
        related_name="game_news",
        on_delete=models.CASCADE,
        help_text="Связь новостей с игрой",
        verbose_name="Игра",
    )
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Заголовок новости",
        verbose_name="Заголовок новости",
    )
    content = models.TextField(
        blank=True,
        help_text="Содержание новости",
        verbose_name="Содержание новости",
    )
    published_date = models.DateTimeField(
        default=timezone.now,
        help_text="Дата и время публикации новости",
        verbose_name="Дата и время публикации новости",
    )

    class Meta:
        """Метаданные о данной модели."""

        verbose_name = "Новости игры"
        verbose_name_plural = "Новости игр"

    def __str__(self):
        """Возвращает строковое представление объекта.

        :return Строковое преставление объекта
        """

        return f"Новость {self.title} по игре {self.game}"
