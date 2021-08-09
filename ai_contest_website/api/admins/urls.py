from django.urls import path
from .user_api import AdminUserList, AdminUserInfo
from .language_api import AdminLanguageList, AdminLanguageInfo

urlpatterns = [
    path('user', AdminUserList.as_view(), name='index'),
    path('user/<str:pk>', AdminUserInfo.as_view(), name='language_info'),

    path('language', AdminLanguageList.as_view(), name='index'),
    path('language/<str:pk>', AdminLanguageInfo.as_view(), name='language_info'),
]