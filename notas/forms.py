from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo','conteudo']
        labels = {
            'titulo': 'Título',
            'conteudo': 'Conteúdo'
        }