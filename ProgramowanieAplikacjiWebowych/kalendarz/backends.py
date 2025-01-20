from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.db.models import Q

class EmailOrUsernameAuthBackend(BaseBackend):
    from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrUsernameAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticate a user by their email or username.
        """
        try:
            # Try to fetch the user by email
            user = User.objects.filter(email=username).first()
            if not user:
                # If no user found by email, try by username
                user = User.objects.filter(username=username).first()

            # Check the password if user exists
            if user and user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

