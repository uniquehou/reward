from django.conf.urls import url
from first import views

app_name = "first"
urlpatterns = [
    url(r'questionnaire', views.Questionnaire.as_view(), name='questionnaire'),

    url(r'search/', views.search.as_view(), name='search'),
    url(r'codeExchange/', views.codeExchange, name='codeExchange'),
    url(r'ClickMap/', views.onClickMap.as_view(), name='clickmap'),
    url(r'getlock/', views.getLock.as_view(), name='getlock'),
    url(r'^lock/', views.lock, name='lock'),
    url(r'^unlock/', views.unlock, name="unlock"),
]