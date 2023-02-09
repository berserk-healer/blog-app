from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment
# Register your models here.


class PostAdmin(SummernoteModelAdmin):

    summernote_fields = '__all__'
    list_display = ('title', 'author', 'created_on')
    list_filter = ("author",)
    search_fields = ['title', 'content']


class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name',)



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
