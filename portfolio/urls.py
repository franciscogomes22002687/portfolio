from django.shortcuts import render
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import  static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='apresentacao'),
    path('formacao', views.formacao_view, name='formacao'),
    path('projetos', views.projetos_view, name='projetos'),
    path('competencias', views.competencias_view, name='competencias'),
    path('blog', views.blog_view, name='blog'),
    path('login', views.login_view, name='login'),
    path('contact', views.contact_view, name='contact')
]

urlpatterns += staticfiles_urlpatterns()