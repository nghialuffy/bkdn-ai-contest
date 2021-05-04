from django.urls import path

from api.api_views.problem_api import ProblemInfo, ProblemList, ProblemUpload

urlpatterns = [
    # ex: /polls/
    path('', ProblemList.as_view(), name='problem_list'),
    path('<str:pk>/', ProblemInfo.as_view(), name='problem_info'),
    path('upload/', ProblemUpload.as_view(), name='upload')
]