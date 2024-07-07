from django.urls import path
from . import views


urlpatterns = [
    path('mensajes/lista',views.ListaMensajes.as_view(), name='lista_mensajes'),
    path('mensajes/<int:pk>/',views.VerMensaje.as_view(), name='ver_mensaje'),
    path('mensajes/crear',views.CrearMensaje.as_view(), name='crear_mensaje'),
    path('mensajes/<int:pk>/editar',views.EditarMensaje.as_view(), name='editar_mensaje'),
    path('mensajes/<int:pk>/eliminar',views.EliminarMensaje.as_view(), name='eliminar_mensaje'),
    
    
    
  
]

