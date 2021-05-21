from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    # ex: /polls/
    path('refresh', TokenRefreshView.as_view(), name='refresh_token'),
    # path('<int:pk>/', language_api.detail_item, name='detail'),
]
