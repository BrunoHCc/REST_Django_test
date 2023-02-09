from django.contrib import admin
from django.urls import path

from Academia.views import listaClientes

urlpatterns = [
    path('outro/', listaClientes),
]