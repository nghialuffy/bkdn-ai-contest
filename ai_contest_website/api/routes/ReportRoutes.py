from django.urls import path

from api.api_views.report_api import ReportApi

urlpatterns = [
    path('', ReportApi.as_view(), name='index')
]