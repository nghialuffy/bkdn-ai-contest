from django.urls import path

from api import views
from api.api_views import language_api

urlpatterns = [
    # ex: /polls/
    path('', language_api.index, name='index'),
]