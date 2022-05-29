from django.shortcuts import render
from . import views
from django.urls import path

app_name = "portfolio"

urlpatterns = [
    path('apresentacao', views.home_page_view, name='apresentacao'),
    path('formacao', views.formacao, name='formacao'),
    path('projetos', views.projetos, name='projetos'),
    path('competencias', views.competencias, name='competencias'),
]