from django.db import models


class Game(models.Model):
    """Модель игры."""

    game = models.CharField(
        unique=True,
        max_length=255,
        null=False,
        help_text="Название игры",
        verbose_name="Игра"
    )
    game_studio = models.ForeignKey(
        "StudioDeveloper",
        related_name="studio_game",
        on_delete=models.PROTECT,
        help_text="Связь игры со студией",
        verbose_name="Студия",
    )
    genre = models.ForeignKey(
        "Genre",
        related_name="genre_game",
        on_delete=models.PROTECT,
        help_text="Связь игры с жанром",
        verbose_name="Жанр",
    )
    release_date = models.DateField(
        blank=True,
        help_text="Дата релиза игры",
        verbose_name="Дата релиза",
    )
    description = models.TextField(
        blank=True,
        help_text="Подробное описание игры",
        verbose_name="Описание",
    )
    rating = models.PositiveSmallIntegerField(
        blank=True,
        help_text="Рейтинг игры",
        verbose_name="Рейтинг",
    )
    system_requirements = models.JSONField(
        blank=True,
        help_text="Системные требования игры",
        verbose_name="Системные требования",
    )

    class Meta:
        """Метаданные данной модели."""

        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def __str__(self):
        """Возвращает строковое представление объекта.

        :return Строковое преставление объекта
        """

        return self.game
