from django.urls import path

from api import views
from api.api_views import  ContestList, ContestInfo

urlpatterns = [
    # ex: /polls/
    path('', ContestList.as_view(), name='index'),
    path('<str:pk>/', ContestInfo.as_view(), name='contest_detail'),
]