# Generated by Django 5.0.2 on 2024-02-24 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(db_index=True, help_text='Название жанра', max_length=255, verbose_name='Жанр')),
                ('description', models.TextField(blank=True, help_text='Подробное описание жанра', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='StudioDeveloper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studio_developer', models.CharField(db_index=True, help_text='Название студии', max_length=255, verbose_name='Студия')),
                ('site', models.URLField(blank=True, help_text='Сайт разработчика', verbose_name='Сайт')),
                ('description', models.TextField(blank=True, help_text='Подробное описание студии', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Студия',
                'verbose_name_plural': 'Студии',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(db_index=True, help_text='Название игры', max_length=255, verbose_name='Игра')),
                ('release_date', models.DateField(blank=True, help_text='Дата релиза игры', verbose_name='Дата релиза')),
                ('description', models.TextField(blank=True, help_text='Подробное описание игры', verbose_name='Описание')),
                ('rating', models.PositiveSmallIntegerField(blank=True, help_text='Рейтинг игры', verbose_name='Рейтинг')),
                ('system_requirements', models.JSONField(blank=True, help_text='Системные требования игры', verbose_name='Системные требования')),
                ('genre', models.ForeignKey(help_text='Связь игры с жанром', on_delete=django.db.models.deletion.PROTECT, related_name='genre_game', to='game.genre', verbose_name='Жанр')),
                ('game_studio', models.ForeignKey(help_text='Связь игры со студией', on_delete=django.db.models.deletion.PROTECT, related_name='studio_game', to='game.studiodeveloper', verbose_name='Студия')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
    ]