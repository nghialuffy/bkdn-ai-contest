from django.urls import path

from api.api_views import UserLoginView, UserRegisterView, UserList, UserInfo

urlpatterns = [
    path('', UserList.as_view(), name='index'),
    path('<str:pk>/', UserInfo.as_view(), name='user_detail'),
]