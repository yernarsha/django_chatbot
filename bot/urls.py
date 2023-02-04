from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('getResponse', views.getResponse, name="getResponse"),
]
