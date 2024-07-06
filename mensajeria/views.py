from django.shortcuts import render
from mensajeria.models import Mensaje
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

   
class CrearMensaje(LoginRequiredMixin,CreateView):
    model = Mensaje
    template_name = 'mensajeria/crear_mensaje.html'
    success_url = reverse_lazy('lista_mensajes')
    fields = '__all__'


class EliminarMensaje(LoginRequiredMixin,DeleteView):
    model = Mensaje
    template_name = 'servicios/eliminar_mensaje.html'
    success_url = reverse_lazy('mensajes')

  
class ListaMensajes(LoginRequiredMixin,ListView):
    model = Mensaje
    template_name = 'mensajeria/lista_mensaje.html'
    
    
    
  