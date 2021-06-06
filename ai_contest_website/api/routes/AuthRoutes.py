from django.urls import path

from api import views
from api.api_views import  UserInfoLogin
from api.api_views import AdminPermissionAuthorization
from api.api_views import OrganizerPermissionAuthorization

urlpatterns = [
    # ex: /polls/
    path('userinfo', UserInfoLogin.as_view(), name='index'),
    path('admin', AdminPermissionAuthorization.as_view(), name='admin_permission_auth'),
    path('organizer', OrganizerPermissionAuthorization.as_view(), name='organizer_permission_auth')
    # path('<str:pk>/', ContestInfo.as_view(), name='contest_detail'),
]
