from django.urls import path

from api import views
from api.api_views import  HtmlDocumentApi, SampleCodeHelp

urlpatterns = [
    # ex: /polls/
    # path('html/', HtmlDocumentApi.as_view(), name='html'),
    path('sample-code', SampleCodeHelp.as_view(), name='sample_code_help')
]