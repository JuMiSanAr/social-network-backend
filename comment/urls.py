from django.urls import path

from comment.views import GetCreateCommentView, GetCommentsByUserView, DeleteUpdateCommentView
from post.views import PostsView, PostView, ToggleLikeView, UserPostsView

urlpatterns = [
    path('<int:pk>/', GetCreateCommentView.as_view()),
    path('change-delete/<int:pk>/', DeleteUpdateCommentView.as_view()),
    path('me/', GetCommentsByUserView.as_view()),
    ]
