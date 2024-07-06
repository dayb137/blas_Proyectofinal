from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mensaje(models.Model):
    email = models.EmailField()
    mensaje = models.TextField(max_length=500)
    creado_el = models.DateTimeField(auto_now_add=True) 
    
     
    def __str__(self):
        return f'{self.email} {self.mensaje} {self.creado_el}'