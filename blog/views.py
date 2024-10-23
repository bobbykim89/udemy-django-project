from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.

class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# def starting_page(req):
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     return render(req, 'blog/index.html', context={
#         'posts': latest_posts
#     })


class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


# def posts(req):
#     all_posts = Post.objects.all().order_by('-date')
#     return render(req, 'blog/all-posts.html', context={
#         'all_posts': all_posts
#     })

class SinglPostView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        return context


# def post_detail(req, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(req, 'blog/post-detail.html', context={
#         'post': identified_post,
#         'post_tags': identified_post.tags.all()
#     })
