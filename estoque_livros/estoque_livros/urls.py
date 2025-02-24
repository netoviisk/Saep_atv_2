from django.urls import path
from livros import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('autor/', views.cadastrar_autor, name='cadastrar_autor'),
    path('livro/', views.cadastrar_livro, name='cadastrar_livro'),
    path('lista/', views.lista_cadastros, name='lista_cadastros'),
]