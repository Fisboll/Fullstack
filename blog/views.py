from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Post


class HomePage (TemplateView):
    """
    Renders home page
    """
    template_name = 'index.html'


class Playstation (TemplateView):
    """
    Render Playstation page
    """
    template_name = 'playstation.html'


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_at")
    template_name = "index.html"
    paginate_by = 6
