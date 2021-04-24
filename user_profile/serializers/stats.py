from rest_framework import serializers

from user.serializers.nested_basic import UserNestedBasicSerializer
from user_profile.models import UserProfile


class UserProfileStatsSerializer(serializers.ModelSerializer):

    user = UserNestedBasicSerializer()

    posts = serializers.SerializerMethodField()
    friends = serializers.SerializerMethodField()
    liked_posts = serializers.SerializerMethodField()
    times_liked = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()


    def get_posts(self, instance):
        return len(instance.posts.all())

    def get_friends(self, instance):
        return len(instance.friends_with.all())

    def get_liked_posts(self, instance):
        return len(instance.liked_posts.all())

    def get_times_liked(self, instance):
        my_posts = instance.posts.all()
        result = 0
        for post in my_posts:
            result += len(post.liked_by.all())
        return result

    def get_following(self, instance):
        return len(instance.following.all())

    def get_followers(self, instance):
        return len(instance.followers.all())

    def get_comments(self, instance):
        return len(instance.comments.all())

    class Meta:
        model = UserProfile
        fields = ['user', 'posts', 'friends', 'liked_posts', 'times_liked', 'following', 'followers', 'comments']
