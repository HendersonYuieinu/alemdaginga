from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Postagem


# Create your views here.
def home_blog(request):
    postagens = Postagem.objects.all().order_by('data_criacao')
    contexto = {
        'postagens' : postagens
    }
    return render(request, 'blog/index.html', contexto)

def sobre_blog(request):
    return render(request, 'blog/sobre.html' )

def eventos_index(request):
    return render(request, 'blog/eventos-index.html')

def post_completo(request, slug):
    post = get_object_or_404(Postagem, slug=slug)
    contexto = {
        'post' : post
    }
    
    return render(request, 'blog/template.html', contexto)