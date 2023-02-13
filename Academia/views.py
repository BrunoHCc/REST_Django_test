from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import AlunoSerializer

from Academia.models import Aulas, Aluno
# Create your views here.

def listaClientes(request):
    
    aulas = Aulas.objects.all()
    print(list(aulas))
    html = "<html><body>"
    for x in list(aulas):
        html += f"<h2> Aula de {x.name} - ministrada pelo(a) prof {x.prof.name} </h2>"

    html += "</body></html>"

    return HttpResponse(html)

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer