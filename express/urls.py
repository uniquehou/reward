from django.conf.urls import url
from express import views

app_name = "express"
urlpatterns = [
    url(r'reserve/', views.Reserve.as_view(), name='reserve'),

]