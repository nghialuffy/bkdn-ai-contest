# init urls for organizer
from django.urls import path, include
from .contest_api import UserContestRegister, UserContestUnregister
from .rank_api import UserContestRank
from .user_api import UserListAttendedContests

urlpatterns = [
    path('contest/register/<str:contest_id>', UserContestRegister.as_view(), name='register_contest'),
    path('contest/unregister/<str:contest_id>', UserContestUnregister.as_view(), name='unregister_contest'),
    path('contest/<str:contest_id>/rank', UserContestRank.as_view(), name='contest_rank'),
    # User
    path('user/<str:user_id>/attended_contest', UserListAttendedContests.as_view(), name='list_attended_contests')
]