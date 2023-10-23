from django.db import models
from .validators import validation_nombre_cliente, validation_nombre_farmaceutico, validacion_precio_medicamento

# Create your models here.
class Farmaceutico(models.Model):
    nombre = models.CharField(max_length=100, validators=[validation_nombre_farmaceutico,])
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    ci = models.CharField(max_length=40)

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100, validators=[validation_nombre_cliente,])
    nit = models.CharField(max_length=50)

class MedicamentoUnits(models.TextChoices):
    SOBRE = 's', 'Sobres'
    COMPRIMIDO = 'comp', 'Comprimidos'
    AMPOLLA = 'amp', 'Ampollas'
    FRASCO = 'fr', 'Frascos'
    UNGUENTO = 'un', 'Unguentos'

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    pais_procedencia = models.CharField(max_length=100)
    unidades = models.CharField(max_length=10, choices=MedicamentoUnits.choices)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, validators=[validacion_precio_medicamento,])
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Factura(models.Model):
    numero_factura = models.CharField(max_length=100)
    codigo_autorizacion = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    nombre_empresa = models.CharField(max_length=100)
    nit_empresa = models.CharField(max_length=50)
    farmaceutico = models.ForeignKey(Farmaceutico, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class MedicamentoFactura(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
