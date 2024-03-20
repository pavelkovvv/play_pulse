from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, UserInfo

admin.site.register(CustomUser, UserAdmin)
admin.site.register(UserInfo)
