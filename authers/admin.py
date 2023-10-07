from django.contrib import admin
from authers.models import Auther


@admin.register(Auther)
class AutherAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'birth_date']
