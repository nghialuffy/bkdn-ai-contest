from django.contrib import admin
from django.urls import path, include
from api.api_views import UserLoginView, UserRegisterView

urlpatterns = [
    path('organizer/', include('api.organizer.urls'), name='organizer'),

    path('language/', include('api.routes.LanguageRoutes'), name='language'),
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
    # path('ranking/', include('api.routes.RankingRoutes'), name='ranking')

    
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]