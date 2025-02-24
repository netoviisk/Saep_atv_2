from django.db import models

class Autor(models.Model):
    nome_completo = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)  # Agora opcional

    def __str__(self):
        return self.nome_completo

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    edicao = models.CharField(max_length=50)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    preco_capa = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="livros")

    def __str__(self):
        return f"{self.titulo} ({self.ano_publicacao})"

class Estoque(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="estoque")
    quantidade = models.PositiveIntegerField()  # Evita números negativos
    data_entrada = models.DateField(auto_now_add=True)  # Padrão: data atual
    data_saida = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.livro.titulo} - {self.quantidade} unidades"
