from django.shortcuts import render
import datetime

def home_page_view(request):
    return render(request, 'portfolio/apresentacao.html')


def formacao(request):
    return render(request, 'portfolio/formacao.html')

def projetos(request):
    return render(request, 'portfolio/projetos.html')

def competencias(request):
    return render(request, 'portfolio/competencias.html')



