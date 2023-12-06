from django.contrib import admin

from surdo.models import AppUser, Task, Answer


# Register your models here.


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
