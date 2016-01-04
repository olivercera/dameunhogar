from adopcion.models import Mascota
from rest_framework import viewsets
from api.serializers import MascotaSerializer


class MascotaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
