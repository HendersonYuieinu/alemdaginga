from django.db import models
from django.utils.text import slugify

# Create your models here. 
    
class Postagem(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    subtitulo = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    conteudo = models.TextField()
    resumo = models.TextField(max_length=300, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    capa = models.ImageField(upload_to='posts/capa/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
        
         
    def __str__(self):
        return self.titulo



class Evento(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    descricao = models.TextField()
    resumo = models.TextField(max_length=500, blank=True, null=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    local = models.CharField(max_length=200)
    capa = models.ImageField(upload_to='eventos/capa/', blank=True, null=True)
    valor = models.CharField(max_length=50, default='Gratuito')
    status = models.CharField(max_length=20, default='Confirmado')
    link_inscricao = models.URLField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.titulo
    

class Integrante(models.Model):
    nome = models.CharField(max_length=50)
    tag = models.CharField(max_length=30)
    biografia = models.TextField()
    foto = models.ImageField(upload_to='integrantes/', blank=True, null=True)
    x = models.URLField() 
    facebook = models.URLField()
    instagram = models.URLField()
    
    def __str__(self):
        return self.nome