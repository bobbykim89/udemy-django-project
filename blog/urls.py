from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.starting_page, name='starting-page'),
    path("posts", view=views.posts, name='posts-page'),
    path('posts/<slug:slug>', view=views.post_detail,
         name='post-detail-page')  # /posts/my-post
]
