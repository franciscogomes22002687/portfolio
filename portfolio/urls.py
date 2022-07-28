from django.shortcuts import render
from . import views
from django.urls import path

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='apresentacao'),
    path('formacao', views.formacao_view, name='formacao'),
    path('projetos', views.projetos_view, name='projetos'),
    path('competencias', views.competencias_view, name='competencias'),
    path('blog', views.blog_view, name='blog'),
]