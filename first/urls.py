from django.conf.urls import url
from first import views

urlpatterns = [
    url(r'^transphone/', views.trans_phone, name='transphone'),
    url(r'questionnaire', views.Questionnaire.as_view(), name='questionnaire'),

    url(r'clickmap/', views.clickMap.as_view()),
    url(r'drawaward/', views.drawAward.as_view(), name='drawaard'),
    url(r'search/', views.search.as_view(), name='search'),

    url(r'meng/', views.meng, name='meng'),

    url(r'ClickMap/', views.onClickMap.as_view(), name='clickmap'),
]