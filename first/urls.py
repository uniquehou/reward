from django.conf.urls import url
from first import views

urlpatterns = [
    url(r'^transphone/', views.trans_phone, name='transphone'),
    url(r'questionnaire', views.Questionnaire.as_view(), name='questionnaire'),

    url(r'clickmap/', views.clickMap.as_view(), name='clickmap'),
    url(r'drawaward/', views.drawAward.as_view(), name='drawaard'),
]