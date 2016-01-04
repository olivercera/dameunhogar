from adopcion.models import Mascota
from rest_framework import serializers


class MascotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascota
        fields = ('url', 'nombre')