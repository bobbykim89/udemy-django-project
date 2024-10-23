from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.StartingPageView.as_view(), name='starting-page'),
    path("posts", view=views.AllPostsView.as_view(), name='posts-page'),
    path('posts/<slug:slug>', view=views.SinglPostView.as_view(),
         name='post-detail-page')  # /posts/my-post
]
