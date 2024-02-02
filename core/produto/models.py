from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='nome')
    preco = models.CharField(max_length=100, verbose_name='preco')
    descricao = models.TextField(verbose_name='descricao')
    # imagem = models.ImageField(upload_to='')
    cultivo = models.BooleanField()
    modocultivo = models.CharField(max_length=100, verbose_name='modocultivo')
    floracao = models.BooleanField()
    epocafloracao = models.CharField(max_length=100, verbose_name='epocafloracao')

    def __str__(self):
        return self.nome
