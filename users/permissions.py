from rest_framework.permissions import BasePermission

from centers.models import CenterUser
from .models import USER_ROLE_CHOICES


class IsCenterUser(BasePermission):
    """
    Allows access only to regular users.
    """
    def has_permission(self, request, view):
        is_regular_user = bool(request.user and request.user.is_authenticated and request.user.role == USER_ROLE_CHOICES.USER)
        if is_regular_user:
            try:
                CenterUser.objects.get(user=request.user)
                return True
            except CenterUser.DoesNotExist:
                return False
        return False

class IsObserver(BasePermission):
    """
    Allows access only to observers.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == USER_ROLE_CHOICES.OBSERVER)

class IsPrisonDirector(BasePermission):
    """
    Allows access only to prison directors.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == USER_ROLE_CHOICES.PRISON_DIRECTOR)