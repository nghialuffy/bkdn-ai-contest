from django.urls import path

from api.api_views import problem_api

urlpatterns = [
    # ex: /polls/
    path('', problem_api.index, name='index'),
]