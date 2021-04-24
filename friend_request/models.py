from django.db import models

# Create your tests here.
from user_profile.models import UserProfile


class FriendRequest(models.Model):

    CHOICES = [('A', 'Accepted'), ('R', 'Rejected'), ('P', 'Pending')]

    status = models.CharField(max_length=1, default='P', choices=CHOICES)

    received_by = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='received_friend_requests')
    sent_by = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='sent_friend_requests')

    resolved_time = models.DateTimeField(auto_now=True)
