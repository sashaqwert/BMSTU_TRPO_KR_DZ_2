from django.contrib import admin

from surdo.models import AppUser


# Register your models here.


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass