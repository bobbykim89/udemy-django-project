from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.views.generic import ListView
from .forms import CommentForm
from django.views import View


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

class SinglPostView(View):
    def get(self, req, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id')
        }
        return render(request=req, template_name='blog/post-detail.html', context=context)

    def post(self, req, slug):
        comment_form = CommentForm(req.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id')
        }
        return render(request=req, template_name='blog/post-detail.html', context=context)

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context['post_tags'] = self.object.tags.all()
    #     context['comment_form'] = CommentForm()
    #     return context


# def post_detail(req, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(req, 'blog/post-detail.html', context={
#         'post': identified_post,
#         'post_tags': identified_post.tags.all()
#     })

class ReadLaterView(View):
    def get(self, req):
        stored_posts = req.session.get('stored_posts')

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True
        return render(req, 'blog/stored-posts.html', context=context)

    def post(self, req):
        stored_posts = req.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []

        post_id = int(req.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            req.session['stored_posts'] = stored_posts

        return HttpResponseRedirect('/')
