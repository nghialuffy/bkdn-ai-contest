from django.urls import path

from api.api_views.language_api import *

urlpatterns = [
    # ex: /polls/
    path('', LanguageList.as_view(), name='index'),
    path('<str:pk>/', LanguageInfo.as_view(), name='language_info'),
    # path('<int:pk>/', language_api.detail_item, name='detail'),
]