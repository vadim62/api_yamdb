from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'bio')}),
        ('Permissions', {'fields': ('role',)}),
    )
    list_display = ('email', 'username')
    search_fields = ('email', 'username')
    list_filter = ('email', 'username')
    ordering = ('email', 'username')
    empty_value_display = '-пусто-'


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('name',)
    list_filter = ('id',)


models = apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
