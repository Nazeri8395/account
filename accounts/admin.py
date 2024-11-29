from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Customer

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['first_name', 'last_name', 'email', 'username', 'is_active',]
    add_fieldsets = (
    (
        None,
        {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "email"),
        },
    ),
)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',]
    list_per_page = 10
    ordering = ['user__last_name', 'user__first_name',]
    search_fields = ['user__last_name__istartswith', 'user__first_name__istartswith',]
    
    
