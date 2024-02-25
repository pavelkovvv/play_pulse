# Generated by Django 5.0.2 on 2024-02-25 18:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Заголовок новости', max_length=100, verbose_name='Заголовок новости')),
                ('content', models.TextField(blank=True, help_text='Содержание новости', verbose_name='Содержание новости')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Дата и время публикации новости', verbose_name='Дата и время публикации новости')),
                ('game', models.ForeignKey(help_text='Связь новостей с игрой', on_delete=django.db.models.deletion.CASCADE, related_name='game_news', to='game.game', verbose_name='Игра')),
            ],
            options={
                'verbose_name': 'Новости игры',
                'verbose_name_plural': 'Новости игр',
            },
        ),
    ]