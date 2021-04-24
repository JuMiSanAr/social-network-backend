from django.urls import path

from post.views import PostsView, PostView, ToggleLikeView, UserPostsView, PostsFromFollowingView, OtherUserPostsView, \
    PostsFromFriendsView, PostsLikedView

urlpatterns = [
    path('', PostsView.as_view()),
    path('<int:pk>/', PostView.as_view()),
    path('user/me/', UserPostsView.as_view()),
    path('user/<int:pk>/', OtherUserPostsView.as_view()),
    path('toggle-like/<int:pk>/', ToggleLikeView.as_view()),
    path('following/', PostsFromFollowingView.as_view()),
    path('friends/', PostsFromFriendsView.as_view()),
    path('likes/', PostsLikedView.as_view()),
    ]
