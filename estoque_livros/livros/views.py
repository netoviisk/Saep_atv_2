from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Autor, Estoque
from .forms import LivroForm, AutorForm, EstoqueForm


# Página inicial
def index(request):
    return render(request, 'index.html')


# Cadastro de Autor
def cadastro_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cadastros')  # Redireciona para a lista de cadastros
    else:
        form = AutorForm()

    return render(request, 'cadastro_autor.html', {'form': form})


# Cadastro de Livro
def cadastro_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cadastros')  # Redireciona para a lista de livros
    else:
        form = LivroForm()

    return render(request, 'cadastro_livro.html', {'form': form})


# Lista de Cadastros
def lista_cadastros(request):
    livros = Livro.objects.select_related('autor').all()  # Busca os livros com seus autores
    return render(request, 'lista_cadastros.html', {'livros': livros})


# Editar Autor
def editar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)

    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_cadastros')  # Redireciona após editar

    else:
        form = AutorForm(instance=autor)

    return render(request, "editar_autor.html", {"form": form, "autor": autor})


# Excluir Autor (remove o autor e todos os seus livros)
def excluir_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.delete()  # Exclui o autor e, por cascade, seus livros
    return redirect("lista_cadastros")


# Editar Livro
def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_cadastros')  # Redireciona após editar

    else:
        form = LivroForm(instance=livro)

    return render(request, "editar_livro.html", {"form": form, "livro": livro})


# Excluir Livro (apaga um único livro)
def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    livro.delete()  # Exclui apenas o livro
    return redirect('lista_cadastros')

def estoque(request, livro_id=None):
    if livro_id:
        # Exibe o estoque de um livro específico
        livro = get_object_or_404(Livro, id=livro_id)
        estoques = Estoque.objects.filter(livro=livro)
        return render(request, 'estoque.html', {'livro': livro, 'estoques': estoques})
    else:
        # Exibe todos os estoques
        estoques = Estoque.objects.all()
        return render(request, 'estoque.html', {'estoques': estoques})

def adicionar_estoque(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == "POST":
        form = EstoqueForm(request.POST)
        if form.is_valid():
            estoque = form.save(commit=False)
            estoque.livro = livro
            estoque.save()
            return redirect('estoque', livro_id=livro_id)
    else:
        form = EstoqueForm()

    return render(request, 'adicionar_estoque.html', {'form': form, 'livro': livro})