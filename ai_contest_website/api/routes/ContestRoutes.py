from django.urls import path

from api import views
from api.api_views import  ContestList, ContestInfo, AttendedContest

urlpatterns = [
    # ex: /polls/
    path('', ContestList.as_view(), name='index'),
    path('user/<id>/', AttendedContest.as_view(), name='user_attended'),
    path('<str:pk>/', ContestInfo.as_view(), name='contest_detail'),
]