from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    model = CustomUser
    list_display = ["phone_number","email", "username","name"]

admin.site.register(CustomUser, CustomUserAdmin)