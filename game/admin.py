from django.contrib import admin

from game.models.game import Game
from game.models.genre import Genre
from game.models.studio_developer import StudioDeveloper

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(StudioDeveloper)
