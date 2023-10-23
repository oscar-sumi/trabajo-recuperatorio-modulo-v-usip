from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Farmaceutico, Cliente, Medicamento
from .serializers import FarmaceuticoSerializer, ClienteSerializer, MedicamentoSerializer
# Create your views here.

def index(request):
    return HttpResponse("Hola Proyecto Recuperatorio")

class FarmaceuticoViewSet(viewsets.ModelViewSet):
    queryset = Farmaceutico.objects.all()
    serializer_class = FarmaceuticoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

@api_view(["GET"])
def farmaceuticos_cantidad(request):
    """
    Cantidad de Empleados Farmaceuticos registrados en la tabla
    """
    try:
        farmaceuticos_cantidad = Farmaceutico.objects.count()
        return JsonResponse(
            {"farmaceuticos_cantidad": farmaceuticos_cantidad},
            safe = False,
            status = 200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, safe=False, status = 500)


@api_view(["GET"])
def medicamentos_hechosen_bolivia(request):
    """
    Medicamentos cuyo pais de procedencia es BOLIVIA
    """
    try:
        medicamentos = Medicamento.objects.filter(pais_procedencia='Bolivia')
        return JsonResponse(
            MedicamentoSerializer(medicamentos, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, safe=False, status=400)