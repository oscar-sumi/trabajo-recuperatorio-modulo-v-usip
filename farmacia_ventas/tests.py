from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Farmaceutico, Cliente, Medicamento

# Create your tests here.
class TestFarmaceuticos(TestCase):
    def test_creacion_farmaceutico(self):
        with self.assertRaises(ValidationError) as qv:
            q = Farmaceutico.objects.create(nombre="admin")
            q.full_clean()

        mensaje_error = dict(qv.exception)
        self.assertEqual(mensaje_error["nombre"][0], "No esta permitido usar la palabra admin como nombre")

class TestClientes(TestCase):
    def test_creacion_cliente(self):
        q = Cliente.objects.create(nombre_completo="cliente")
        self.assertRaises(ValidationError, q.full_clean)

class TestMedicamentos(TestCase):
    def test_insercion_medicamento(self):
        q = Medicamento(nombre="Amoxicilina de 1000 mg")
        q.save()
        self.assertEqual(Medicamento.objects.count(), 1)