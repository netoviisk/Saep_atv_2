from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('cadastrar_autor/', views.cadastrar_autor, name='cadastrar_autor'),  # Cadastro de Autor
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),  # Cadastro de Livro
    path('lista_cadastros/', views.lista_cadastros, name='lista_cadastros'),  # Listagem de Livros
    path('excluir_autor/<int:autor_id>/', views.excluir_autor, name='excluir_autor'),
    path('excluir_livro/<int:livro_id>/', views.excluir_livro, name='excluir_livro'),
    path('editar_livro/<int:livro_id>/', views.editar_livro, name='editar_livro'),
]
