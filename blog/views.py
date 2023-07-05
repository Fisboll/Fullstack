from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Post, Game, Platform
from .forms import CommentForm


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
    paginate_by = 5


class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.filter(platform='Playstation')
    context_object_name = "game_list"
    template_name = "playstation.html"
    paginate_by = 8


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
                "comments": Comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset)
        comments = post.comments.filter(approved=True).order_by("-created_at")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request):
        post = get_object_or_404(Post)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            pose.likes.add(request.user)
