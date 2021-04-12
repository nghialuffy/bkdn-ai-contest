from django.urls import path

from api import views
from api.api_views.user_api import *

urlpatterns = [
    path('', UserList.as_view(), name='index'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('<str:pk>/', UserList.as_view(), name='user_detail'),
    
]