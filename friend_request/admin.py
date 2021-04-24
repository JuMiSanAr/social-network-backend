from django.contrib import admin

# Register your models here.
from friend_request.models import FriendRequest

admin.site.register(FriendRequest)
ordering = ('id',)
