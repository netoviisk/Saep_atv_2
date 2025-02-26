from django.db import models

class Autor(models.Model):
    nome_completo = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=100, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_completo

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    edicao = models.CharField(max_length=50, blank=True, null=True, verbose_name='Edição')
    editora = models.CharField(max_length=100, blank=True, null=True)
    ano_publicacao = models.IntegerField(blank=True, null=True, verbose_name='Ano de Publicação')
    preco_capa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Preço de Capa')
    categoria = models.CharField(max_length=50, blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')

    def __str__(self):
        return self.titulo

class Estoque(models.Model):
    ENTRADA_SAIDA_CHOICES = [
        ('Entrada', 'Entrada'),
        ('Saída', 'Saída'),
    ]

    livro = models.ForeignKey('Livro', on_delete=models.CASCADE, related_name='estoque')
    quantidade = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=ENTRADA_SAIDA_CHOICES, db_column='tipo')
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.livro.titulo} - {self.tipo} ({self.quantidade})"