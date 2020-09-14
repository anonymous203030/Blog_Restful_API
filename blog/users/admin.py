from django.contrib import admin

from .models import User, UserProfile


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_verified', 'is_staff', 'is_active', 'created_at', 'updated_at',)
    list_filter = ('is_verified', 'is_staff', 'created_at', 'updated_at', 'is_active',)
    ordering = ('created_at', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_student')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', )

admin.site.register(User, UsersAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday', 'gender', 'owner', )
    list_filter = ('birthday', 'gender', )
    ordering = ('first_name', )

admin.site.register(UserProfile, UserProfileAdmin)
