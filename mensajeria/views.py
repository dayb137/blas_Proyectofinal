from mensajeria.models import Mensaje
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



   
class ListaMensajes(LoginRequiredMixin,ListView):
    model = Mensaje
    template_name = 'mensajeria/lista_mensaje.html'
    context_object_name = 'mensajes'
    
    def get_queryset(self):
        return Mensaje.objects.filter(receptor=self.request.user)
    
class VerMensaje(LoginRequiredMixin,DetailView):
    model = Mensaje
    template_name = 'mensajeria/ver_mensaje.html'
    context_object_name= 'mensaje'
    

class CrearMensaje(LoginRequiredMixin,CreateView):
    model = Mensaje
    template_name = 'mensajeria/crear_mensaje.html'
    success_url = reverse_lazy('lista_mensajes')
    fields = ['receptor','asunto', 'cuerpo']
    
    def form_valid(self, form):
        form.instance.remitente = self.request.user
        return super().form_valid(form)
    
class EditarMensaje(LoginRequiredMixin,UpdateView):
    model = Mensaje
    template_name= 'mensajeria/crear_mensaje.html'
    success_url = reverse_lazy('mensajes')
    
    
class EliminarMensaje(LoginRequiredMixin,DeleteView):
    model = Mensaje
    template_name = 'mensajeria/eliminar_mensaje.html'
    success_url = reverse_lazy('lista_mensajes')
    

  
    
    
  
  