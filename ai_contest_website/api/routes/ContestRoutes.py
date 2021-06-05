from django.urls import path

from api import views
from api.api_views import  ContestList, ContestInfo, AttendedContest, UpcomingContest
from api.api_views import ContestListWithProblems

urlpatterns = [
    # ex: /polls/
    path('', ContestList.as_view(), name='index'),
    path('problems/', ContestListWithProblems.as_view(), name='list_problems'),
    path('user/<id>/', AttendedContest.as_view(), name='user_attended'),
    path('upcoming/', UpcomingContest.as_view(), name='upcoming_contest'),
    path('<str:pk>/', ContestInfo.as_view(), name='contest_detail'),
]
