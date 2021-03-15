from django.contrib import admin

from .models import Posts, UserPostRelation


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'created_at', 'owner',)
    filter_horizontal = ()
    list_filter = ('updated_at', 'created_at', 'title', 'owner',)
    ordering = ('created_at',)

    search_fields = ('title', 'description', 'owner',)


admin.site.register(Posts, PostAdmin)


class UserPostRelationAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'like', 'saved', 'rating', 'reacted_at',)
    filter_horizontal = ()
    list_filter = ('rating', 'saved', 'like', 'reacted_at',)
    ordering = ('reacted_at',)

    search_fields = ('user', 'post',)


admin.site.register(UserPostRelation, UserPostRelationAdmin)
