from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Servicio
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class Publicaciones(ListView):
     model = Servicio
     template_name ='servicios/listado_de_publis.html'
     context_object_name = 'publi'
     

class CrearPubli(LoginRequiredMixin,CreateView):
    model = Servicio
    template_name ='servicios/crear_publi.html'
    success_url = reverse_lazy('publi')
    fields = '__all__'
    
class EditarPubli(LoginRequiredMixin,UpdateView):
    model = Servicio
    template_name ='servicios/editar_publi.html'
    success_url = reverse_lazy('publi')
    fields = '__all__'

class VerPubli(DetailView):
    model = Servicio
    template_name = 'servicios/ver_publi.html'

    
class EliminarPubli(LoginRequiredMixin,DeleteView):
    model = Servicio
    template_name = 'servicios/eliminar_publi.html'
    success_url = reverse_lazy('publi')
    
class BuscarPubli(ListView):
    model = Servicio
    context_object_name = 'publi'

    def get_queryset(self):
        criterio = self.request.GET.get('criterio')
        result = Servicio.objects.filter(Servicionombre__icontains=criterio).all()
        return result
    
    
