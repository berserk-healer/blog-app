from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):

    search_fields = ('email', 'username', 'first_name', 'last_name',)
    list_filter = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff',)
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff')
    fieldsets = (
        ('Required', {'fields': ('email', 'username', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Personal', {'fields': ('age', 'description','profile_image',)}),
    )
    add_fieldsets = (
        ('Required', {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_active','is_staff',)}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)