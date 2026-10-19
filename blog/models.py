from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    
class Postagem(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    subtitulo = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    conteudo = models.TextField()
    resumo = models.TextField(max_length=300, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, max_length=100)
    capa = models.ImageField(upload_to='posts/capa/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
        
         
    def __str__(self):
        return self.titulo
