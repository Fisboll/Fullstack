from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Post, Game, Platform


class HomePage (TemplateView):
    """
    Renders home page
    """
    template_name = 'index.html'


class Playstation (generic.ListView):
    """
    Render Playstation page
    """
    model = Game
    queryset = Game.objects.filter(platform='Playstation')
    queryset = Game.objects.filter(platform='Xbox')
    template_name = 'playstation.html'


class PlatformList(generic.ListView):
    model = Platform
    context_object_name = "platform_list"
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset)
        comments = post.comment.filter(approved=True).order_by('created_at')
        liked = False
        if post.likes.filter(id=self.request.user.id).exist():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            }
        )
