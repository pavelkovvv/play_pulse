from django.db import models


class StudioDeveloper(models.Model):
    """Модель студии-разработчика."""

    studio_developer = models.CharField(
        db_index=True,
        max_length=255,
        null=False,
        help_text='Название студии',
        verbose_name='Студия',
    )
    site = models.URLField(blank=True, help_text='Сайт разработчика', verbose_name='Сайт')
    description = models.TextField(blank=True, help_text='Подробное описание студии', verbose_name='Описание')

    class Meta:
        """Человекочитаемое название для экземпляра модели."""

        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'

    def __str__(self):
        """Возвращает строковое представление объекта.

        :return Строковое преставление объекта
        """
        return self.studio_developer
