from django.contrib.auth import get_user_model

# Create your views here.
from django.db.models import Q
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveAPIView
from user.serializers.default import UserDetailedSerializer
from Helpers.permissions_main import UserPermissions

User = get_user_model()


# Get all users information
class UsersView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailedSerializer

    def get_queryset(self):
        try:
            search = self.request.query_params.get('search')
            return User.objects.filter(Q(username__icontains=search) |
                                           Q(email__icontains=search) |
                                           Q(first_name__icontains=search) |
                                           Q(last_name__icontains=search))
        except ValueError:
            return User.objects.all()


# Get other user info
class OtherUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailedSerializer


# Get the information about the logged-in user and update logged-in user
class MyUserView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailedSerializer
    permission_classes = [UserPermissions]

    def get_object(self):
        return self.request.user
