from django.contrib import admin

from .models import Posts, UserPostRelation

class MultiDBAdminModel(admin.ModelAdmin):
    using = "posts_db"

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


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'created_at', 'owner', )
    filter_horizontal = ()
    list_filter = ('updated_at', 'created_at', 'title', 'owner', )
    ordering = ('created_at', )

    search_fields = ('title', 'description', 'owner', )

admin.site.register(Posts, PostAdmin)

class UserPostRelationAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'like', 'saved', 'rating', 'reacted_at', )
    filter_horizontal = ()
    list_filter = ('rating', 'saved', 'like', 'reacted_at', )
    ordering = ('reacted_at', )

    search_fields = ('user', 'post', )

admin.site.register(UserPostRelation, UserPostRelationAdmin)
