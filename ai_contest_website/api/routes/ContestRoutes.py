from django.urls import path

from api import views
from api.api_views import contest_api

urlpatterns = [
    # ex: /polls/
    path('', contest_api.index, name='index'),
]