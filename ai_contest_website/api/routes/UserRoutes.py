from django.urls import path

from api.api_views import UserList, UserInfo, UserListAttendedContest, JoinContest

urlpatterns = [
    path('', UserList.as_view(), name='index'),
    path('attended-contest/<str:pk>', UserListAttendedContest.as_view(), name='index'),
    path('join-contest', JoinContest.as_view(), name='join_contest'),
    path('<str:pk>/', UserInfo.as_view(), name='user_detail'),
]