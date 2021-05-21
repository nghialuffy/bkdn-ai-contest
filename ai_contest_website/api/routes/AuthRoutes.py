from django.urls import path

from api import views
from api.api_views import  UserInfoLogin

urlpatterns = [
    # ex: /polls/
    path('userinfo', UserInfoLogin.as_view(), name='index'),
    # path('<str:pk>/', ContestInfo.as_view(), name='contest_detail'),
]
