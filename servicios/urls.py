from django.urls import path
from . import views

urlpatterns = [
    
     path('servicios/',views.Publicaciones.as_view(), name='publi'),
     path('servicios/crear',views.CrearPubli.as_view(), name='crear_publi'),
     path('servicios/<int:pk>',views.VerPubli.as_view(), name='ver_publi'),
     path('servicios/<int:pk>',views.EditarPubli.as_view(), name='editar_publi'),
     path('servicios/<int:pk>',views.EliminarPubli.as_view(), name='eliminar_publi'),
     
]
