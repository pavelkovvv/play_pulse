from django.db import models


class Genre(models.Model):
    """Модель жанра."""

    genre = models.CharField(db_index=True, max_length=255, null=False, help_text='Название жанра', verbose_name='Жанр')
    description = models.TextField(blank=True, help_text='Подробное описание жанра', verbose_name='Описание')

    class Meta:
        """Человекочитаемое название для экземпляра модели."""

        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        """Возарвщает строковое представление объекта.

        :return Строковое представление объекта.
        """
        return self.genre
