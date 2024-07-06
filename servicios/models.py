from django.db import models


# Create your models here.


class Servicio(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media',null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    
   
    def __str__(self):
        return f'{self.Nombre} {self.fecha}'
   
    def image_url(self):
        return self.image.url if self.image else ''


    