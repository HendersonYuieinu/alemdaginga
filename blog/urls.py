from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_blog, name='home'),
    path('sobre', views.sobre_blog, name='sobre'),
    path('eventos', views.eventos_index, name='eventos')
]
