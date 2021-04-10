from django.urls import path, include


urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # ex: /polls/5/
    path('language/', include('api.routes.LanguageRoutes'), name='language'),
    path('user/', include('api.routes.UserRoutes'), name='user'),
    path('contest/', include('api.routes.ContestRoutes'), name='contest'),
    path('problem/', include('api.routes.ProblemRoutes'), name='problem'),
    path('result/', include('api.routes.ResultRoutes'), name='result'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]