import os

from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView
from rest_framework.response import Response

from registration.models import Registration
from registration.serializers.serializers import RegistrationSerializer
from django.core.mail import send_mail
from uuid import uuid4
from user.models import User
from user_profile.models import UserProfile


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = []

    def perform_create(self, serializer):
        email = self.request.data["email"]
        code = uuid4()

        send_mail(
            'Motion registration code',
            f'Your registration code for the Motion Website is : {code}',
            os.environ.get('DEFAULT_FROM_EMAIL'),
            [email],
            fail_silently=False,
        )
        new_user = User(email=email, username=code)
        new_user.save()
        new_profile = UserProfile(user=new_user)
        new_profile.save()
        serializer.save(code=code, user=new_profile)


class ValidationView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = []

    def patch(self, request, *args, **kwargs):
        passed_code = self.request.data["code"]
        registration = Registration.objects.get(id=self.request.data["id"])
        user_profile = UserProfile.objects.get(id=registration.user_id)
        user = User.objects.get(id=user_profile.user_id)
        if passed_code == registration.code:
            registration.used = True
            registration.save()
            user.email = self.request.data["email"]
            user.username = self.request.data["username"]
            user.first_name = self.request.data["first_name"]
            user.last_name = self.request.data["last_name"]
            user.password = make_password(self.request.data["password"])
            user.save()
            return Response("code matched successfully")
        else:
            return Response("", status=401)


class PasswordResetView(UpdateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = []

    def patch(self, request, *args, **kwargs):
        try:
            user = User.objects.get(email=self.request.data['email'])
            data = {
                'code': uuid4(),
                'used': False,
                'action': 'PR',
                'email': request.data['email']
            }
            serializer = self.get_serializer(user.profile.code, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(code=data['code'])
            send_mail(  # don't forget to change the url for resetting the password!!!
                'Password reset code',
                f"Here is your code for resetting your password {data['code']} \n Click this link to reset https://david.eve.juan.propulsion-learn.ch/password-reset/validation/",
                os.environ.get('DEFAULT_FROM_EMAIL'),
                [user.email],
                fail_silently=False,
            )
            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            raise ValidationError(message='Please enter a valid e-mail')


class PasswordResetValidationView(UpdateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = []

    def patch(self, request, *args, **kwargs):
        code_from_request = request.data['code']
        try:
            code_from_request_obj = Registration.objects.get(code=code_from_request)
            user = code_from_request_obj.user
            is_code_used = code_from_request_obj.used

            if request.data['password1'] == request.data['password2'] and code_from_request_obj and not is_code_used:
                # is_code_used = True
                user.user.password = make_password(request.data['password1'])
                user.user.save()
                code_from_request_obj.used = True
                code_from_request_obj.save()
                return Response(status=status.HTTP_200_OK)
            elif request.data['password1'] != request.data['password2']:
                return Response({'error': 'Two passwords given are not the same'}, status=status.HTTP_418_IM_A_TEAPOT)
            elif is_code_used:
                return Response({'error': 'This code is already used'}, status=status.HTTP_418_IM_A_TEAPOT)
        except Registration.DoesNotExist:
            raise ValidationError(message='This code is invalid. Please, enter a valid code')
