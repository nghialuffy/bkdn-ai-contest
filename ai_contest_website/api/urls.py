from django.contrib import admin
from django.urls import path, include
from api.api_views import UserLoginView, UserRegisterView

urlpatterns = [
    path('admin/', include('api.admins.urls'), name='admin'),
    path('nuser/', include('api.user.urls'), name='nuser'),
    path('organizer/', include('api.organizer.urls'), name='organizer'),
    

    path('user/', include('api.routes.UserRoutes'), name='user'),
    path('contest/', include('api.routes.ContestRoutes'), name='contest'),
    path('problem/', include('api.routes.ProblemRoutes'), name='problem'),
    path('result/', include('api.routes.ResultRoutes'), name='result'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('token/', include('api.routes.TokenRoutes'), name='token'),
    path('auth/', include('api.routes.AuthRoutes'), name='auth'),
    path('document/', include('api.routes.DocumentRoutes'), name='document'),
    path('report/', include('api.routes.ReportRoutes'), name='report'),
]