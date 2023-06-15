from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from portfolio.models import TFC, BlogPost, Cadeira, Competencia, Escola, Interesse, Lingua, Projeto
from .forms import *

def home_page_view(request):
    return render(request, 'portfolio/apresentacao.html')


def formacao_view(request):
    return render(request, 'portfolio/formacao.html')

def projetos_view(request):
    context = {'projetos': Projeto.objects.all(),
                'tfcs': TFC.objects.all()}

    return render(request, 'portfolio/projetos.html', context)

def competencias_view(request):
    context = {'competencias': Competencia.objects.all(),
                'cadeiras': Cadeira.objects.order_by('ano', 'semestre'),
                'escolas': Escola.objects.order_by('ano_inicio').reverse(),
                'linguas': Lingua.objects.all(),
                'interesses': Interesse.objects.all()}

    return render(request, 'portfolio/competencias.html', context)

def blog_view(request):

    blog_posts = BlogPost.objects.all()

    blog_posts = sorted(blog_posts, key=lambda i: i.date, reverse=True)

    return render(request, 'portfolio/blog.html', {'blog_posts': blog_posts})

def login_view(request):

    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'portfolio/apresentacao.html')
        else:
            return render(request, 'portfolio/apresentacao.html', {'message': 'Login Failed: Your user ID or password is incorrect.'})


    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'You were disconnected.'
    })

def contact_view(request):
    return render(request, 'portfolio/contact.html')

def newCadeira_view(request):
    form = CadeiraForm(request.POST or None)

    if form.is_valid():
        form.save()
        render(request, 'portfolio/competencias.html')

    context = {'form':form}
    return render(request, 'portfolio/newCadeira.html', context)

def newSkill_view(request):
    form = SkillForm(request.POST or None)

    if form.is_valid():
        form.save()
        render(request, 'portfolio/competencias.html')

    context = {'form':form}
    return render(request, 'portfolio/newSkill.html', context)

def newEducation_view(request):
    form = EducationForm(request.POST or None)

    if form.is_valid():
        form.save()
        render(request, 'portfolio/competencias.html')

    context = {'form':form}
    return render(request, 'portfolio/newSkill.html', context)

def newLanguage_view(request):
    form = LanguageForm(request.POST or None)

    if form.is_valid():
        form.save()
        render(request, 'portfolio/competencias.html')

    context = {'form':form}
    return render(request, 'portfolio/newLanguage.html', context)

def newHobby_view(request):
    form = HobbyForm(request.POST or None)

    if form.is_valid():
        form.save()
        render(request, 'portfolio/competencias.html')

    context = {'form':form}
    return render(request, 'portfolio/newHobby.html', context)