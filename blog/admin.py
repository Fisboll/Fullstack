from django.contrib import admin
from .models import Post, Game, Comment, User_profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):

    Summernote_fields = ('content')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_filler = ('status', 'created_on')
    list_display = ('subgrenres', 'title')
    seatch_fields = ['foreign_key_realted_fieldname']
    Summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    Summernote_fields = ('content')


@admin.register(User_profile)
class User_profileAdmin(SummernoteModelAdmin):

    Summernote_fields = ('content')
