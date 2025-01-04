from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status','created_on', 'updated_on',)
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):

    list_display = ('author', 'body', 'approved', 'created_on')
    list_filter = ('approved','updated_on',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)