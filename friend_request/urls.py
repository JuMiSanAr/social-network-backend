from django.urls import path

from friend_request.views import NewFriendRequestView, FriendRequestView, PendingFriendRequestsView

urlpatterns = [
    path('request/<int:pk>/', NewFriendRequestView.as_view()),
    path('requests/<int:pk>/', FriendRequestView.as_view()),
    path('requests/pending/', PendingFriendRequestsView.as_view()),
    ]
