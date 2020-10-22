from django.contrib import admin

from .models import User, UserProfile

class MultiDBAdminModel(admin.ModelAdmin):
    using = "users_db"

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_verified', 'is_staff', 'is_active', 'created_at', 'updated_at',)
    list_filter = ('is_verified', 'is_staff', 'created_at', 'updated_at', 'is_active',)
    ordering = ('created_at', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff',)}),
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
    list_filter = ('birthday', 'gender','owner' )
    ordering = ('first_name', )

admin.site.register(UserProfile, UserProfileAdmin)
