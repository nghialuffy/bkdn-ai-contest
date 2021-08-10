# init urls for organizer
from django.urls import path, include
from .contest_api import UserContestRegister, UserContestUnregister, UserContestList, UserContestInfo
from .problem_api import UserProblemsOnContestId
from .rank_api import UserContestRank
from .user_api import UserListRegisterContests
from .rank_ws import UserContestRankWebsocket
from .result_ws import UserResultWebsocket


urlpatterns = [
    path('contest/register/<str:contest_id>', UserContestRegister.as_view(), name='register_contest'),
    path('contest/unregister/<str:contest_id>', UserContestUnregister.as_view(), name='unregister_contest'),
    path('contest/<str:contest_id>/rank', UserContestRank.as_view(), name='contest_rank'),
    path('contest/<str:contest_id>', UserContestInfo.as_view(), name='contest_info'),
    path('contest', UserContestList.as_view(), name='contest_list'),
    path('problem', UserProblemsOnContestId.as_view(), name='contest_problems'),
    # User
    path('user/<str:user_id>/contest', UserListRegisterContests.as_view(), name='list_attended_contests')
]

ws_urlpatterns = [
    path('ws/contest/<str:contest_id>/rank', UserContestRankWebsocket.as_asgi(), name='contest_rank'),
    path('ws/result/<str:result_id>', UserResultWebsocket.as_asgi(), name='result'),
]