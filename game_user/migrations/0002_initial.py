# Generated by Django 5.0.2 on 2024-02-25 18:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game_user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='gameuser',
            name='user',
            field=models.ForeignKey(help_text='Связь игры пользователя с пользователем', on_delete=django.db.models.deletion.CASCADE, related_name='user_gameuser', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
