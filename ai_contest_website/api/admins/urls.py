from django.urls import path
from .language_api import AdminLanguageList, AdminLanguageInfo

urlpatterns = [
    path('language', AdminLanguageList.as_view(), name='index'),
    path('language/<str:pk>', AdminLanguageInfo.as_view(), name='language_info'),
]