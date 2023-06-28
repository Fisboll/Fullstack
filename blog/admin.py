from django.contrib import admin
from .models import Post, Game, Comment, User_profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):

    Summernote_fields = ('content')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'subtitle', 'created_by')
    seatch_fields = ['title', 'content']
    prepopulated_fields = {'title': ('title', 'subtitle')}
    list_filler = ('status', 'created_at')
    Summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'post', 'created_at')
    list_filter = ('created_at', 'name')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']


@admin.register(User_profile)
class User_profileAdmin(SummernoteModelAdmin):

    Summernote_fields = ('content')
