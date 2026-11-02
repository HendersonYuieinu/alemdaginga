from django.contrib import admin
from .models import Postagem,Integrante, Evento
# Register your models here.

admin.site.register(Postagem)
admin.site.register(Evento)
admin.site.register(Integrante)