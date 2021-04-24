from django.urls import path

from user.views import UsersView, MyUserView, OtherUserView

urlpatterns = [
    path('', UsersView.as_view()),
    path('me/', MyUserView.as_view()),
    path('<int:pk>/', OtherUserView.as_view())
    ]
