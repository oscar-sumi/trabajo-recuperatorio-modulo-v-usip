from django.contrib import admin

# Register your models here.
from .models import Farmaceutico
from .models import Cliente
from .models import Medicamento
from .models import Factura

admin.site.register(Factura)

class FarmaceuticoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'direccion', 'telefono', 'ci')
    ordering = ['nombre']
    search_fields = ['nombre', 'ci']

admin.site.register(Farmaceutico, FarmaceuticoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'nit')
    ordering = ['nombre_completo']
    search_fields = ['nit']

admin.site.register(Cliente, ClienteAdmin)

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fabricante', 'pais_procedencia', 'unidades', 'precio', 'disponible')
    ordering = ['nombre']
    search_fields = ['nombre']
    list_filter = ['disponible']

admin.site.register(Medicamento, MedicamentoAdmin)