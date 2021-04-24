
# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

# List all posts and create a new post
from rest_framework.response import Response

from Helpers.permissions_main import FriendRequestPermissions
from friend_request.Serializers.default import FriendRequestSerializer
from friend_request.models import FriendRequest
from user_profile.models import UserProfile

from django.db.models import Q


# Send friend request
class NewFriendRequestView(CreateAPIView):
    serializer_class = FriendRequestSerializer

    def create(self, request, *args, **kwargs):

        receiving_user = UserProfile.objects.get(id=self.kwargs['pk'])

        if receiving_user == self.request.user.profile:
            return Response({"error": "you can't add yourself as a friend"},
                            status=status.HTTP_409_CONFLICT)

        for request in self.request.user.profile.sent_friend_requests.values():
            if request['received_by_id'] == receiving_user.id:
                return Response({'error': 'you already sent a friend request to this user'},
                                status=status.HTTP_409_CONFLICT)

        for request in self.request.user.profile.received_friend_requests.values():
            if request['sent_by_id'] == receiving_user.id:
                return Response({"error": "this user has already sent you a friend request"},
                                status=status.HTTP_409_CONFLICT)

        serializer = self.get_serializer(data=kwargs)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, receiving_user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, receiving_user):
        serializer.save(sent_by=self.request.user.profile, received_by=receiving_user)


# Get info about friend request, accept or reject friend request, delete friend request
class FriendRequestView(RetrieveUpdateDestroyAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [FriendRequestPermissions]

    def get_queryset(self):
        return FriendRequest.objects.filter(id=self.kwargs['pk'])

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.status == 'P':
            if request.data['status'] == 'P':
                return Response({'invalid': 'only accepted ("A") and rejected ("P") statuses allowed in this request'},
                                status=status.HTTP_400_BAD_REQUEST)

            partial = kwargs.pop('partial', False)
            serializer = self.get_serializer(instance, data=kwargs, partial=partial)
            serializer.is_valid(raise_exception=True)

            if request.data['status'] == 'A':
                self.perform_update(serializer, 'A')
                requester = instance.sent_by
                request.user.profile.friends_with.add(requester)

            elif request.data['status'] == 'R':
                self.perform_update(serializer, 'R')

            return Response(self.get_serializer(instance).data)

        else:
            return Response({'invalid': 'this friend request has already been resolved'},
                            status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer, new_status):
        serializer.save(status=new_status)


# List all pending friend requests
class PendingFriendRequestsView(ListAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(Q(status='P') &
                                            (Q(sent_by=self.request.user.profile) |
                                            Q(received_by=self.request.user.profile)))
