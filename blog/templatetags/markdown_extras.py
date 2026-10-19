from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter(name='markdown')

def dp_markdown(text):
    # Converte o texto markdown em HTML seguro para a tela
    return mark_safe(markdown.markdown(text, extensions=['fenced_code', 'codehilite']))