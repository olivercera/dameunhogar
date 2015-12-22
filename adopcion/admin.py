from django.contrib import admin

# Register your models here.
from .models import Mascota

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_pub')

admin.site.register(Mascota, MascotaAdmin)