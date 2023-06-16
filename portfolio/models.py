from distutils.command.upload import upload
from email.mime import image
from pickle import TRUE
from tkinter import CASCADE
from django.utils import timezone
from django.db import models
from django.forms import CharField, DateTimeField, IntegerField

class BlogPost(models.Model):
    title = models.CharField(max_length=50, default='')
    text = models.TextField(max_length=500, default='')
    author = models.CharField(max_length=50, default='')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Professor(models.Model):
    nome = models.CharField(max_length=30)
    linkedin = models.URLField(blank=True)
    lusofona = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Escola(models.Model):
    nome = models.CharField(max_length=50)
    ano_inicio = models.IntegerField()
    ano_fim = models.IntegerField()

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    nome = models.CharField(max_length = 40)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.CharField(max_length=500)
    docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
    docente_pratica = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="pratico")

    def __str__(self):
        return self.nome
    

class Competencia(models.Model):
    titulo = models.CharField(max_length=40)
    image = models.ImageField(blank=True, upload_to="portfolio/static/portfolio/images/skill_images")

    def __str__(self):
        return self.titulo


class Interesse(models.Model):
    titulo = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo


class Lingua(models.Model):
    nome = models.CharField(max_length=30)
    grau = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField(blank=True, upload_to="portfolio/static/portfolio/images/project_images")
    ano = models.IntegerField()
    link_github = models.CharField(max_length=30, blank=True)


class TFC(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=400)
    alunos = models.ManyToManyField(Pessoa)
    orientadores = models.ManyToManyField(Professor)
    ano = models.IntegerField()
    imagem = models.ImageField(blank=True, upload_to="portfolio/static/portfolio/images/TFC_images")
    linkGithub = models.CharField(max_length=500)
    linkYoutube = models.CharField(max_length=500)
    relatorio = models.CharField(max_length=500)

    def __str__(self):
        return self.titulo
