from django.shortcuts import render, redirect
from .models import Livro, Autor, Estoque
from .forms import LivroForm, AutorForm, EstoqueForm

def index(request):
    return render(request, 'index.html')

# Cadastro de Autor
def cadastrar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_autor')
    else:
        form = AutorForm()
    return render(request, 'cadastro_autor.html', {'form': form})

# Cadastro de Livro
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cadastros')
    else:
        form = LivroForm()
    return render(request, 'cadastro_livro.html', {'form': form})

# Lista de Cadastros
def lista_cadastros(request):
    livros = Livro.objects.select_related('autor').all()
    return render(request, 'lista_cadastros.html', {'livros': livros})
