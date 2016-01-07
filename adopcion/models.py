from __future__ import unicode_literals

from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    raza = models.CharField(max_length=80)
    fecha_pub = models.DateTimeField('fecha publicacion', auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.nombre