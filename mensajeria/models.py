from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name='Mensajes_enviados', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='Mensajes_recibidos', on_delete=models.CASCADE)  
    asunto = models.CharField(max_length=250, default='Asunto')
    cuerpo = models.TextField()
    fecha = models.DateTimeField()

     
    def __str__(self):
        return self.asunto