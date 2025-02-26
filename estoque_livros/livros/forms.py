from django import forms
from .models import Autor, Livro, Estoque

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome_completo', 'nacionalidade', 'biografia']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'isbn', 'edicao', 'editora', 'ano_publicacao', 'preco_capa', 'categoria', 'autor']


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['livro', 'quantidade', 'tipo', 'data', 'valor']