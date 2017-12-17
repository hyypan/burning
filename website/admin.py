from django.contrib import admin

# Register your models here.
from website import models as m


@admin.register(m.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('password', 'username')


@admin.register(m.Articles)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
