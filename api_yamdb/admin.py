from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()


class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', ),
        }),
    )
    list_display = ('email', 'username')
    list_filter = ('email', 'username')
    search_fields = ('email', 'username')
    ordering = ('email', 'username')
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
