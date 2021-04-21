from django.urls import path

from api.api_views.result_api import ResultList, ResultInfo
urlpatterns = [
    # ex: /polls/
    path('', ResultList.as_view(), name='result_list'),
    path('<str:pk>', ResultInfo.as_view(), name='result_info'),
]