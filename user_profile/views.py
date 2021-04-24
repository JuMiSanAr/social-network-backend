
# Create your views here.
from rest_framework.generics import GenericAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from user_profile.models import UserProfile
from user_profile.serializers.followers_serializer import UserProfileFollowersSerializer
from user_profile.serializers.nested import UserProfileNestedSerializer
from user_profile.serializers.stats import UserProfileStatsSerializer


# Get my user info
class UserStatsView(GenericAPIView):
    serializer_class = UserProfileStatsSerializer

    def get(self, request, *args, **kwargs):
        logged_in_user = UserProfile.objects.get(id=request.user.profile.id)
        self.check_object_permissions(self.request, logged_in_user)
        serializer = self.get_serializer(logged_in_user)
        return Response(serializer.data)


# Follow or unfollow user
class ToggleFollowView(UpdateAPIView):
    serializer_class = UserProfileFollowersSerializer

    def update(self, request, *args, **kwargs):
        user_to_follow = UserProfile.objects.get(id=kwargs['pk'])
        users_following = user_to_follow.followers.values()

        if len(users_following) == 0:
            user_to_follow.followers.add(request.user.profile)
            return Response(self.get_serializer(user_to_follow).data)

        for user in users_following:
            if user['user_id'] == request.user.id:
                user_to_follow.followers.remove(request.user.profile)
                return Response(self.get_serializer(user_to_follow).data)

        user_to_follow.followers.add(request.user.profile)
        return Response(self.get_serializer(user_to_follow).data)


# Get list of followers
class GetMyFollowersView(ListAPIView):
    serializer_class = UserProfileNestedSerializer

    def get_queryset(self):
        followers = self.request.user.profile.followers.all()
        return followers


# Get list of users I follow
class GetFollowingView(ListAPIView):
    serializer_class = UserProfileNestedSerializer

    def get_queryset(self):
        following = self.request.user.profile.following.all()
        return following


# Get list of friends
class GetFriendsView(ListAPIView):
    serializer_class = UserProfileNestedSerializer

    def get_queryset(self):
        friends = self.request.user.profile.friends_with.all()
        return friends

