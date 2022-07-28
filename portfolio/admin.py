from django.contrib import admin
from .models import TFC, BlogPost, Cadeira, Competencia, Escola, Interesse, Lingua, Pessoa, Professor, Projeto

admin.site.register(BlogPost)
admin.site.register(Professor)
admin.site.register(Pessoa)
admin.site.register(Escola)
admin.site.register(Cadeira)
admin.site.register(Competencia)
admin.site.register(Interesse)
admin.site.register(Lingua)
admin.site.register(Projeto)
admin.site.register(TFC)



