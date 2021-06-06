from django.urls import path

from api.api_views import  ContestList, ContestInfo, AttendedContest
from api.api_views import ContestListWithProblems, AttendedUser

urlpatterns = [
    # ex: /polls/
    path('', ContestList.as_view(), name='index'),
    path('problems/', ContestListWithProblems.as_view(), name='list_problems'),
    path('user/<id>/', AttendedContest.as_view(), name='list_contests_user_attended'),
    path('<contest_id>/users', AttendedUser.as_view(), name='list_attended_users'),
    path('<str:pk>/', ContestInfo.as_view(), name='contest_detail')
]
