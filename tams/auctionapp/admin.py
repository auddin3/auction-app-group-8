from django.contrib import admin
from .models import User, Product
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

class ProductAdminConfig(admin.ModelAdmin):
    search_fields = ('product_name', 'start_price',)
    ordering = ('start_price',)
    list_display = ('product_name', 'start_price', 'owner',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('product_name', 'description', 'start_price', 'owner',)}),
    )

admin.site.register(User, UserAdminConfig)
admin.site.register(Product, ProductAdminConfig)
