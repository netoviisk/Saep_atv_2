from django.urls import path
from livros import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('cadastro_autor/', views.cadastro_autor, name='cadastro_autor'),  # Cadastro de Autor
    path('cadastro_livro/', views.cadastro_livro, name='cadastro_livro'),  # Cadastro de Livro
    path('lista_cadastros/', views.lista_cadastros, name='lista_cadastros'),  # Listagem de Livros
    path('editar_autor/<int:autor_id>/', views.editar_autor, name='editar_autor'),
    path('excluir_autor/<int:autor_id>/', views.excluir_autor, name='excluir_autor'),
    path('editar_livro/<int:livro_id>/', views.editar_livro, name='editar_livro'),
    path('excluir_livro/<int:livro_id>/', views.excluir_livro, name='excluir_livro'),
    path('estoque/', views.estoque, name='estoque'),
    path('adicionar_estoque/<int:livro_id>/', views.adicionar_estoque, name='adicionar_estoque'),
]
