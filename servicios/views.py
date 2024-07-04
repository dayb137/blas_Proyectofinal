from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Servicio
from django.urls import reverse_lazy


class Publicaciones(ListView):
     model = Servicio
     template_name ='servicios/listado_de_publis.html'
     context_object_name = 'publi'
     

class CrearPubli(CreateView):
    model = Servicio
    template_name ='servicios/crear_publi.html'
    success_url = reverse_lazy('listado_de_publis')
    fields = '__all__'
    
class EditarPubli(UpdateView):
    model = Servicio
    template_name ='servicios/editar_publi.html'
    success_url = reverse_lazy('listado_de_publis')
    fields = '__all__'

class VerPubli(DetailView):
    model = Servicio
    template_name = 'servicios/ver_publi.html'
    
class EliminarPubli(DeleteView):
    model = Servicio
    template_name = 'servicios/eliminar_publi.html'
    success_url = reverse_lazy('listado_de_publis')
    

    
    
