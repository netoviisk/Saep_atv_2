from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Autor
from .forms import LivroForm, AutorForm

# Página inicial
def index(request):
    return render(request, 'index.html')

# Cadastro de Autor
def cadastrar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cadastros')  # Redireciona para a lista de cadastros após salvar
    else:
        form = AutorForm()
    return render(request, 'cadastro_autor.html', {'form': form})

# Cadastro de Livro
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cadastros')  # Redireciona para a lista de livros após salvar
    else:
        form = LivroForm()
    return render(request, 'cadastro_livro.html', {'form': form})

# Lista de Cadastros
def lista_cadastros(request):
    livros = Livro.objects.select_related('autor').all()  # Busca os livros com seus autores
    return render(request, 'lista_cadastros.html', {'livros': livros})

# Excluir Autor (exclui o autor e todos os seus livros)
def excluir_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.delete()  # Exclui o autor e, por cascade, seus livros
    return redirect("lista_cadastros")

# Excluir Livro (apaga um único livro)
def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    livro.delete()  # Exclui apenas o livro
    return redirect('lista_cadastros')  

# Editar Livro
def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_cadastros')  # Redireciona após salvar

    else:
        form = LivroForm(instance=livro)

    return render(request, "editar_livro.html", {"form": form, "livro": livro})
