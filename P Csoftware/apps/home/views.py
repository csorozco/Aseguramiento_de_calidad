from django.shortcuts import render
from django.views.generic import *

from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class indexview(TemplateView):
    template_name='index.html'

class clientesview(TemplateView):
    template_name='clientes.html'

class baseview(TemplateView):
    template_name='layout/base.html'

class articulosview(TemplateView):
    template_name='articulos.html'

class pedidosview(TemplateView):
    template_name='pedidos.html'

class loginview(TemplateView):
    template_name='login.html' 



