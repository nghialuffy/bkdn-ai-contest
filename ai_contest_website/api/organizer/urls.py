# init urls for organizer
from django.urls import path, include
from .contest_api import *
from .problem_api import *
from .language_api import OrganizerLanguageList

urlpatterns = [
    path('contest', OrganizerContestList.as_view(), name='contests_of_organizer'),
    path('contest/<str:contest_id>/contestants', OrganizerListContestants.as_view(), name='contestants_of_contest'),
    path('contest/<str:contest_id>', OrganizerContestInfo.as_view(), name='contest_info'),

    path('contest/<str:contest_id>/problems', OrganizerProblemList.as_view(), name='problems_of_organizer'),
    path('problem/<str:problem_id>', OrganizerProblemInfo.as_view(), name='problem_info'),


    path('language', OrganizerLanguageList.as_view(), name='list_language')

]