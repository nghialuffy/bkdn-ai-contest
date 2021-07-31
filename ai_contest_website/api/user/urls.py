# init urls for organizer
from django.urls import path, include
from .contest_api import UserContestRegister, UserContestUnregister, UserContestList
from .rank_api import UserContestRank
from .user_api import UserListRegisterContests

urlpatterns = [
    path('contest/register/<str:contest_id>', UserContestRegister.as_view(), name='register_contest'),
    path('contest/unregister/<str:contest_id>', UserContestUnregister.as_view(), name='unregister_contest'),
    path('contest/<str:contest_id>/rank', UserContestRank.as_view(), name='contest_rank'),
    path('contest', UserContestList.as_view(), name='contest_list'),
    # User
    path('user/<str:user_id>/contest', UserListRegisterContests.as_view(), name='list_attended_contests')
]