from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Ilha(models.Model):
    ilha = models.CharField(max_length=60)

    def __str__(self):
        return self.ilha

class Concelho(models.Model):
    ilha = models.ForeignKey(Ilha)
    concelho = models.CharField(max_length=60)

    def __str__(self):
        return self.concelho

class Freguesia(models.Model):
    ilha = models.ForeignKey(Ilha)
    concelho = models.ForeignKey(Concelho)
    freguesia = models.CharField(max_length=60)

    def __str__(self):
        return self.freguesia

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    categoria_en = models.CharField(max_length=50)
    categoria_fr = models.CharField(max_length=50)
    categoria_de = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria

class Subcategoria(models.Model):
    categoria = models.ForeignKey(Categoria)
    subcategoria = models.CharField(max_length=50)
    subcategoria_en = models.CharField(max_length=50)
    subcategoria_fr = models.CharField(max_length=50)
    subcategoria_de = models.CharField(max_length=50)

    def __str__(self):
        return self.subcategoria

class Artigo(models.Model):
    titulo = models.CharField(max_length=60)
    titulo_en = models.CharField(max_length=60, blank=True, null=True)
    titulo_fr = models.CharField(max_length=60, blank=True, null=True)
    titulo_de = models.CharField(max_length=60, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    booking = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    ilha = models.ForeignKey(Ilha)
    concelho = models.ForeignKey(Concelho)
    freguesia = models.ForeignKey(Freguesia)
    categoria = models.ForeignKey(Categoria)
    subcategoria = models.ForeignKey(Subcategoria)
    estrelas = models.IntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    telemovel = models.CharField(max_length=15, blank=True, null=True)
    morada = models.CharField(max_length=75)
    imagem = models.FileField(upload_to='articles_images')
    descricao = models.TextField()
    descricao_en = models.TextField(blank=True, null=True)
    descricao_fr = models.TextField(blank=True, null=True)
    descricao_de = models.TextField(blank=True, null=True)
    hora_aberto = models.TimeField(blank=True, null=True)
    hora_fechado = models.TimeField(blank=True, null=True)
    coordenadas_mapa = models.CharField(max_length=50)

class DetalheIlha(models.Model):
    ilha = models.ForeignKey(Ilha)
    historia = HTMLField()
    historia_en = HTMLField(blank=True, null=True)
    historia_fr = HTMLField(blank=True, null=True)
    historia_de = HTMLField(blank=True, null=True)
    numero_concelhos = models.IntegerField()
    numero_freguesias = models.IntegerField()
    video = models.CharField(max_length=100, blank=True, null=True)
    imagem = models.FileField(upload_to='island_images')

class DetalheConcelho(models.Model):
    concelho = models.ForeignKey(Concelho)
    historia = HTMLField()
    historia_en = HTMLField(blank=True, null=True)
    historia_fr = HTMLField(blank=True, null=True)
    historia_de = HTMLField(blank=True, null=True)
    numero_freguesias = models.IntegerField()
    video = models.CharField(max_length=100, blank=True, null=True)
    imagem = models.CharField(max_length=100)

class DetalheFreguesia(models.Model):
    freguesia = models.ForeignKey(Freguesia)
    historia = HTMLField()
    historia_en = HTMLField(blank=True, null=True)
    historia_fr = HTMLField(blank=True, null=True)
    historia_de = HTMLField(blank=True, null=True)
    video = models.CharField(max_length=100, blank=True, null=True)
    imagem = models.FileField(upload_to='location_images')

class Evento(models.Model):
    titulo = models.CharField(max_length=50)
    ilha = models.ForeignKey(Ilha)
    concelho = models.ForeignKey(Concelho)
    freguesia = models.ForeignKey(Freguesia)
    data_comeco = models.DateField()
    data_fim = models.DateField()
    hora_comeco = models.TimeField()
    hora_fim = models.TimeField()
    cartaz = HTMLField(blank=True, null=True)
    imagem = models.FileField(upload_to='city_images')
    video = models.CharField(max_length=100, blank=True, null=True)

class ComidaRegional(models.Model):
    comida = models.CharField(max_length=60)
    receita = models.TextField()
    receita_en = models.TextField(blank=True, null=True)
    receita_fr = models.TextField(blank=True, null=True)
    receita_de = models.TextField(blank=True, null=True)
    restaurante = models.ManyToManyField(Artigo)

class ImagemArtigo(models.Model):
    artigo = models.ForeignKey(Artigo)
    imagem = models.FileField(upload_to='articles_images')

class ImagemIlha(models.Model):
    ilha = models.ForeignKey(Ilha)
    imagem = models.FileField(upload_to='island_images')

class ImagemConcelho(models.Model):
    concelho = models.ForeignKey(Concelho)
    imagem = models.FileField(upload_to='city_images')

class ImagemFreguesia(models.Model):
    freguesia = models.ForeignKey(Freguesia)
    imagem = models.FileField(upload_to='location_images')
