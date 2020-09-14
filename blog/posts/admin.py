from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'created_at', 'owner',)
    filter_horizontal = ()
    list_filter = ('updated_at', 'created_at', 'title', 'owner', )
    ordering = ('created_at', )

    search_fields = ('title', 'description', )

admin.site.register(Post, PostAdmin)