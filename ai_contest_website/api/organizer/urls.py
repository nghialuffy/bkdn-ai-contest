# init urls for organizer
from django.urls import path, include
from .contest_api import *

urlpatterns = [
    path('contest', OrganizerContestList.as_view(), name='contests_of_organizer'),
    path('contest/<str:contest_id>/contestants', OrganizerListContestants.as_view(), name='contest_contestants'),
    path('contest/<str:contest_id>', OrganizerContestInfo.as_view(), name='contest_info') 
]