from django.contrib import admin
from .models import User, Product, Bid
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

class BidAdminConfig(admin.ModelAdmin):
    search_fields = ('id', 'product',)
    ordering = ('end_of_bid',)
    list_display = ('id', 'product', 'end_of_bid',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('product', 'end_of_bid',)}),
    )

admin.site.register(User, UserAdminConfig)
admin.site.register(Product, ProductAdminConfig)
admin.site.register(Bid, BidAdminConfig)
