from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'first_name', 'last_name',)
    ordering = ('-date_of_birth',)
    list_display = ('email', 'username', 'first_name', 
    'last_name', 'is_active')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2',)}),
    )

admin.site.register(User, UserAdminConfig)
