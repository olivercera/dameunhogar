from __future__ import unicode_literals

from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_pub = models.DateTimeField('fecha publicacion')
    
    def __str__(self):
        return self.nombre