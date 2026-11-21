from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Postagem, Evento
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 10)
def home_blog(request):
    postagens = Postagem.objects.all().order_by('-data_criacao')
    contexto = {
        'postagens' : postagens
    }
    return render(request, 'blog/index.html', contexto)

@cache_page(60 * 10)
def eventos_index(request):
    eventos = Evento.objects.all().order_by('-data_inicio')
    contexto = {
        'eventos' : eventos
    }
    return render(request, 'blog/eventos-index.html', contexto)

@cache_page(60 * 10)
def evento_detalhe(request, slug):
    evento = get_object_or_404(Evento, slug=slug)
    contexto = {
        'evento' : evento
    }
    return render(request, 'blog/template_evento.html', contexto)

@cache_page(60 * 10)
def post_completo(request, slug):
    post = get_object_or_404(Postagem, slug=slug)
    contexto = {
        'post' : post
    }
    
    return render(request, 'blog/template.html', contexto)

def sobre_blog(request):
    return render(request, 'blog/sobre.html' )

def integrantes(request):
    return render(request, 'blog/integrantes.html')

def local_treino(request):
    return render(request, 'blog/treinos.html')

def graduacao(request):
    return render(request, 'blog/graduacao.html')   

def health(request):
    return HttpResponse("Hello world")