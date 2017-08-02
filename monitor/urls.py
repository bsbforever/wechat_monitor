from django.conf.urls import  url, include
from monitor import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

