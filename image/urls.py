#TEMP

from django.urls import path

from image.views import ImageView

urlpatterns = [
    path('', ImageView.as_view())
    ]