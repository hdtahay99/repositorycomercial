from django.utils import timezone

from django.shortcuts import render
from .models import Publicacion
# Create your views here.

def listar_pub(request):
    pubs = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html', {'pubs' : pubs})