from rest_framework.serializers import ModelSerializer
from entidad.models import EntidadModel


class EntidadSerializer(ModelSerializer):
    class Meta:
        model = EntidadModel
        # fields = ['id', 'name', 'address', 'phone']
        fields = '__all__'