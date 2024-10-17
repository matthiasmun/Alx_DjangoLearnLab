from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your custom user model with the admin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Customize what fields are shown in the admin interface
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'username')
