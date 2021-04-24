from django.urls import path

from user_profile.views import UserStatsView, ToggleFollowView, GetMyFollowersView, GetFollowingView, GetFriendsView

urlpatterns = [
    path('userstats/', UserStatsView.as_view()),
    path('toggle-follow/<int:pk>/', ToggleFollowView.as_view()),
    path('followers/', GetMyFollowersView.as_view()),
    path('following/', GetFollowingView.as_view()),
    path('friends/', GetFriendsView.as_view())
    ]
