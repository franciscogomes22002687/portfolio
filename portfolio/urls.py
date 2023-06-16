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
    path('logout', views.logout_view, name='logout'),
    path('contact', views.contact_view, name='contact'),
    path('newCadeira', views.newCadeira_view, name='newCadeira'),
    path('newSkill', views.newSkill_view, name='newSkill'),
    path('newEducation', views.newEducation_view, name='newEducation'),
    path('newLanguage', views.newLanguage_view, name='newLanguage'),
    path('newHobby', views.newHobby_view, name='newHobby'),
    path('newProject', views.newProject_view, name='newProject'),
    path('newTFC', views.newTFC_view, name='newTFC'),
    path('newPost', views.newPost_view, name='newPost'),
    path('quizz', views.quizz_view, name='quizz')
]

urlpatterns += staticfiles_urlpatterns()