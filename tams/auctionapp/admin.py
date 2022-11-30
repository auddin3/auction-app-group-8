from django.contrib import admin
from .models import User, Product, Bid, FAQ
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'first_name', 'last_name',)
    ordering = ('-date_of_birth',)
    list_display = ('email', 'username', 'first_name', 
    'last_name',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2',)}),
    )

    fieldsets = (
        (None, {
            'fields': ('email', 'username')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff')
        }),
    )

class ProductAdminConfig(admin.ModelAdmin):
    search_fields = ('product_name', 'start_price',)
    ordering = ('start_price',)
    list_display = ('product_name', 'start_price', 'owner', 'product_image',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('product_name', 'description', 'start_price', 'owner', 'product_image',)}),
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

class FAQAdminConfig(admin.ModelAdmin):
     search_fields = ('question',)
     ordering = ('product',)
     list_display = ('id', 'product', 'question', 'sender')

     add_fieldsets = (
        ("Basic Info", {
            'classes': ('wide',),
            'fields': ('product', 'sender',)}),
        ("Question", {
            'classes': ('wide',),
            'fields': ('question')
        })
    )

admin.site.register(User, UserAdminConfig)
admin.site.register(Product, ProductAdminConfig)
admin.site.register(Bid, BidAdminConfig)
admin.site.register(FAQ, FAQAdminConfig)
