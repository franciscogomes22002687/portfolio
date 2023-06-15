from django.forms import ModelForm
from .models import *

class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

class SkillForm(ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'

class EducationForm(ModelForm):
    class Meta:
        model = Escola
        fields = '__all__'

class LanguageForm(ModelForm):
    class Meta:
        model = Lingua
        fields = '__all__'
        
class HobbyForm(ModelForm):
    class Meta:
        model = Interesse
        fields = '__all__'