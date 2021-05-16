from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.models import TokenUser
from api.models import User
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
class IsSSOAdmin(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        try:
            assert request.user and request.user.is_authenticated
            if request.auth.payload.get('username'):
                return True
            user = request.user
            print(user)
            if isinstance(request.user, TokenUser):
                user_set = User.objects.filter(_id=user.id)
                if user_set.exists():
                    # print('sdfsdf')
                    print(user_set.first().is_admin)
                    user = user_set.first()
                else:
                    return False
            return user.is_admin
        except AssertionError:
            return False


class IsUser(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        try:
            assert request.user and request.user.is_authenticated
            if request.auth.payload.get('username'):
                return True
            user = request.user
            if isinstance(request.user, TokenUser):
                user_set = User.objects.filter(_id=user.id)
                if user_set.exists():
                    user = user_set.first()
                else:
                    return False
            return user
        except AssertionError:
            return False

class IsOrganizer(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        try:
            assert request.user and request.user.is_authenticated
            if request.auth.payload.get('username'):
                return True
            user = request.user
            if isinstance(request.user, TokenUser):
                user_set = User.objects.filter(_id=user.id)
                if user_set.exists():
                    user = user_set.first()
                else:
                    return False
            return IsOrganizer
        except AssertionError:
            return False
class IsOrganizerOrReadOnly(BasePermission):
    """
    The request is authenticated as a Organizer or a read-only request
    """
    def has_permission(self, request, view):
        try:
            assert request.user and request.user.id
            user = User.objects.filter(pk=request.user.id).first()
            print(user.is_organizer)
            return bool (
                request.method in SAFE_METHODS or 
                request.user and
                request.user.is_authenticated and
                user.is_organizer
            )
        except AssertionError:
            return False
        except Exception:
            return False

class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a Organizer or a read-only request
    """
    def has_permission(self, request, view):
        try:
            assert request.user and request.user.id
            user = User.objects.filter(pk=request.user.id).first()
            print(user.is_organizer)
            return bool (
                request.method in SAFE_METHODS or 
                request.user and
                request.user.is_authenticated and
                user.is_admin
            )
        except AssertionError:
            return False
        except Exception:
            return False