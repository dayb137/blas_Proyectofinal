from django.urls import path
from . import views


urlpatterns = [
    path('mensajes/crear',views.CrearMensaje.as_view(), name='crear_mensaje'),
    path('mensajes/lista',views.ListaMensajes.as_view(), name='lista_mensajes'),
    path('mensajes/<int:pk>/delete',views.EliminarMensaje.as_view(), name='eliminar_mensaje'),
  
]

