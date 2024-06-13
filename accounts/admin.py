# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name',
                    'last_name', 'is_staff', 'is_active', ]
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'username', 'last_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    ordering = ['email']  # Use 'email' for ordering


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)