from django.urls import path

from api.api_views import result_api
print("sd")
urlpatterns = [
    # ex: /polls/
    path('', result_api.index, name='index'),
]