# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView

from comment.models import Comment
from comment.serializers.CommentsByUserSerializer import CommentsByUserSerializer
from comment.serializers.default import CommentsDefaultSerializer
from post.models import Post
from Helpers.permissions_main import CommentPermissions


# Post comment
class GetCreateCommentView(ListCreateAPIView):
    serializer_class = CommentsDefaultSerializer

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['pk'])
        serializer.save(user=self.request.user.profile, post=post)

    def get_queryset(self):
        comments = Comment.objects.filter(post=self.kwargs['pk'])
        return comments


# Get comments by user
class GetCommentsByUserView(ListAPIView):
    serializer_class = CommentsByUserSerializer

    def get_queryset(self):
        comments = Comment.objects.filter(user=self.request.user.id)
        return comments


# Delete or update a comment
class DeleteUpdateCommentView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsDefaultSerializer
    permission_classes = [CommentPermissions]
