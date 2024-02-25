from django.db import models


class Genre(models.Model):
    """Модель жанра."""

    genre = models.CharField(
        unique=True,
        max_length=255,
        null=False,
        help_text="Название жанра",
        verbose_name="Жанр"
    )
    description = models.TextField(
        blank=True,
        help_text="Подробное описание жанра",
        verbose_name="Описание"
    )

    class Meta:
        """Метаинформация для данной модели."""

        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        """Возвращает строковое представление объекта.

        :return Строковое представление объекта.
        """

        return self.genre
