from django import forms
from .models import Livro, Autor, Estoque

class LivroForm(forms.ModelForm):
    autor = forms.ModelChoiceField(
        queryset=Autor.objects.all(),
        empty_label="Selecione um autor",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_publicacao': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = '__all__'
        widgets = {
            'livro': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }
