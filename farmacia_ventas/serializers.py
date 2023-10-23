from rest_framework import serializers
from .models import Farmaceutico, Cliente, Medicamento


class FarmaceuticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmaceutico
        fields = "__all__"

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = "__all__"
