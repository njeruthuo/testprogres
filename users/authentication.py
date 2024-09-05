from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import MultipleObjectsReturned


class EmailAuthentication(ModelBackend):
    """
    Custom authentication backend that allows users to log in with either
    their email or username along with their password.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('username')

        try:
            # Try to fetch the user by email or username
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        except MultipleObjectsReturned:
            return None

        # Check the password
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
