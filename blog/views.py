from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home_blog(request):
    return render(request, 'blog/index.html')

def sobre_blog(request):
    return render(request, 'blog/sobre.html' )

def eventos_index(request):
    return render(request, 'blog/eventos-index.html')
    