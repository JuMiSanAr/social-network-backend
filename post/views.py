
# Create your views here.

from django.db.models import Q

from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, RetrieveAPIView, \
    ListAPIView
from rest_framework.response import Response

from image.models import Image
from post.models import Post
from post.serializers.default import PostDetailedSerializer
from post.serializers.nested_likes import PostLikesSerializer
from Helpers.permissions_main import PostPermissions


# List all posts and create a new post
class PostsView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailedSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            shared_post = Post.objects.get(id=self.request.data['shared_post'])
            new_post = serializer.save(posted_by=self.request.user.profile, shared_post=shared_post)

            if request.FILES:
                for file in request.FILES.getlist('image'):
                    new_file = Image(image=file, post=new_post)
                    new_file.save()

        except MultiValueDictKeyError:
            new_post = serializer.save(posted_by=self.request.user.profile)

            if request.FILES:
                for file in request.FILES.getlist('image'):
                    new_file = Image(image=file, post=new_post)
                    new_file.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        try:
            search = self.request.query_params.get('search')
            return Post.objects.filter(Q(content__icontains=search) | Q(posted_by__user__username__icontains=search))
        except ValueError:
            return Post.objects.all()


# Get, update or delete a specific post
class PostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailedSerializer
    permission_classes = [PostPermissions]


# Get all posts from logged-in user
class UserPostsView(ListAPIView):
    serializer_class = PostDetailedSerializer

    def get_queryset(self):
        posts = Post.objects.filter(posted_by=self.request.user.profile.id).order_by('-created')
        return posts


# Get all posts from specific user
class OtherUserPostsView(ListAPIView):
    serializer_class = PostDetailedSerializer

    def get_queryset(self):
        posts = Post.objects.filter(posted_by=self.kwargs.get('pk')).order_by('-created')
        return posts


# Like a post
class ToggleLikeView(UpdateAPIView):
    serializer_class = PostLikesSerializer

    def update(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['pk'])
        users_liked = post.liked_by.values()

        if len(users_liked) == 0:
            post.liked_by.add(request.user.profile)
            return Response(self.get_serializer(post).data)

        for user in users_liked:
            if user['user_id'] == request.user.id:
                post.liked_by.remove(request.user.profile)
                return Response(self.get_serializer(post).data)

        post.liked_by.add(request.user.profile)
        return Response(self.get_serializer(post).data)


# Posts from people that I'm following
class PostsFromFollowingView(ListAPIView):
    serializer_class = PostDetailedSerializer

    def get_queryset(self):
        return Post.objects.filter(posted_by__in=self.request.user.profile.following.all()).order_by('-created')


# Posts from friends
class PostsFromFriendsView(ListAPIView):
    serializer_class = PostDetailedSerializer

    def get_queryset(self):
        return Post.objects.filter(posted_by__in=self.request.user.profile.friends_with.all()).order_by('-created')


# Posts I like
class PostsLikedView(ListAPIView):
    serializer_class = PostDetailedSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        return Post.objects.filter(liked_by=self.request.user.profile).order_by('-created')
