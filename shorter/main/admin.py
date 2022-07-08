from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import ShortUrlModel


@admin.register(ShortUrlModel)
class ShortUrlModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'long_url', 'short_url')
