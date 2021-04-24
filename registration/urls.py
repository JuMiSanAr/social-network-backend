from django.urls import path
from registration.views import RegistrationView, PasswordResetView, PasswordResetValidationView
from registration.views import ValidationView

urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('registration/validation/', ValidationView.as_view()),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset/validation/', PasswordResetValidationView.as_view())
]
