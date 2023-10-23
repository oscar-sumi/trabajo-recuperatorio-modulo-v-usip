# INSTRUCCIONES PARA USAR EL API REST SISTEMA DE VENTAS PARA FARMACIA

## 1. Datos del Autor

Nombre: Oscar Aldo Sumi Zamorano
Participante Modulo V - DIPLOMADO EN FULLSTACK DEVELOPER BACK END Y FRONT END (CUARTA VERSIÓN) - USIP

El proyecto denominado farmacia consta de una aplicación llamada farmacia_ventas

## 2. Descripción de la Base de Datos

La Base de Datos consta de las siguientes tablas:
- Famaceutico: Lista de los funcionarios de la farmacia encargados de realizar la venta de los medicamentos.
- Cliente: Lista de personas que realizan la compra de medicamentos.
- Medicamento: Lista de medicamentos que oferta la farmacia.
- Factura: Lista de las facturas generadas por la venta de medicamentos.
- MedicamentoFactura: Tabla que relaciona a las facturas emitidas con los medicamentos vendidos.

Se han creado modelos para cada una de estas tablas.

## 3. Credenciales del Superusuario Administrador

Para acceder a la interfaz de administración de proyecto se deben usar las siguientes credenciales de acceso

```sh
- Usuario: oscar.sumi
- Contraseña: Recuperatorio
```

## 4. Validaciones Personalizadas

Se han creado tres validaciones personalizadas que son:
- Tabla Farmaceutico: No se permite la inserción de un funcionario farmacéutico cuyo nombre sea "admin".
- Tabla Cliente: No se permite la inserción de un cliente cuyo nombre sea "cliente".
- Tabla Medicamento: No se permite la inserción de medicamento con precio 0.

Para probar las validaciones personalizadas haciendo uso de un cliente que consuma el servico API-REST del proyecto (Postman o similar) abrir las siguientes URLs:

- Validación 1: Tabla Farmaceutico
Haciendo uso del verbo POST ir a la siguiente URL:

```sh
URL: http://127.0.0.1:8000/farmacia_ventas/farmaceuticos/
```

y en el body enviar el siguiente objeto JSON:

```sh
{
    "nombre": "admin",
    "apellido_paterno": "Perez",
    "apellido_materno": "Gomez",
    "direccion": "Av. Juan Pablo",
    "telefono": "74651389",
    "ci": "43259784"
}
```

El API responderá devolviendo el siguiente mensaje:

```sh
{
    "nombre": [
        "No esta permitido usar la palabra admin como nombre"
    ]
}
```

- Validación 2: Tabla Cliente
Haciendo uso del verbo POST ir a la siguiente URL

```sh
URL: http://127.0.0.1:8000/farmacia_ventas/clientes/
```

y en el body enviar el siguiente objeto JSON:

```sh
{
    "nombre_completo": "cliente",
    "nit": "01073534322"
}
```

El API responderá devolviendo el siguiente mensaje:

```sh
{
    "nombre_completo": [
        "No esta permitido usar la palabra cliente como nombre"
    ]
}
```

- Validación 3: Tabla Medicamento
Haciendo uso del verbo POST ir a la siguiente Url:

```sh
URL: http://127.0.0.1:8000/farmacia_ventas/medicamentos/
```

y en el body enviar el siguiente objeto JSON:

```sh
{
    "nombre": "Revidox",
    "fabricante": "Genomalab",
    "pais_procedencia": "Mexico",
    "unidades": "comp",
    "precio": "0",
    "disponible": "True"
}
```

El API responderá devolviendo el siguiente mensaje:

```sh
{
    "precio": [
        "El precio del medicamento no puede ser 0"
    ]
}
```

## 5. Test Unitarios o de Integración

Se han efectuado los siguientes Tests Unitarios:
- TestFarmaceuticos: En la tabla Farmaceutico se está verificando que el validador personalizado del nombre del farmacéutico devuelva el siguiente mensaje: "No esta permitido usar la palabra admin como nombre"

- TestClientes: En la tabla Clientes se está verificando que el validador personalizado no permita la creación de un cliente de nombre "cliente"

- TestMedicamentos: En la tabla Medicamentos se está verificando que sea posible la inserción de un nuevo medicamento

## 6. Registro de Modelos en el Administrador de Django

En el archivo admin.py se han registrado los siguientes modelos:
- Farmaceutico
- Cliente
- Medicamento
- Factura

tal como se puede apreciar:
```sh
from .models import Farmaceutico
from .models import Cliente
from .models import Medicamento
from .models import Factura

admin.site.register(Factura)
admin.site.register(Farmaceutico, FarmaceuticoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
```

Líneas 4, 5, 6, 7, 9, 16, 23, 31 respectivamente

## 7. Django Rest Framework - Creación de 3 ModelViewSet

Se han creado 3 ModelViewSet para los modelos: Farmaceutico, Cliente y Medicamento, asimismo se los ha documentado haciendo uso de la herramienta Swagger, para verificar la creación de los ModelViewSet mencionados ir a la siguiente url:

```sh
URL: http://127.0.0.1:8000/apidoc/
```

## 8. Creación de un Custom API

Se han creado 2 Custom APIs que son:
- farmaceuticos_cantidad: Determina la cantidad de funcionarios farmacéuticos registrados en la tabla Farmaceutico
- medicamentos_hechosen_bolivia: Muestra un listado de los medicamentos de procedencia boliviana

Para probar los Custom APIs haciendo uso de un cliente que consuma el servico API-REST del proyecto (Postman o similar) abrir las siguientes URLs:

- Custom Api: farmaceuticos_cantidad
Haciendo uso del verbo GET ir a la siguiente URL:

```sh
URL: http://127.0.0.1:8000/farmacia_ventas/farmaceuticos/cantidad/
```

El API responderá devolviendo el siguiente objeto JSON:

```sh
{
    "farmaceuticos_cantidad": 12
}
```

- Custom Api: medicamentos_hechosen_bolivia
Haciendo uso del verbo GET ir a la siguiente URL:

```sh
URL: http://127.0.0.1:8000/farmacia_ventas/medicamentos/hechosen/bolivia/
```

El API responderá devolviendo mostrando un listado de todos los medicamentos cuyo pais de origen es Bolivia:

```sh
[
    {
        "id": 1,
        "nombre": "Paracetamol de 200 mg",
        "fabricante": "Laboratorios Inti",
        "pais_procedencia": "Bolivia",
        "unidades": "comp",
        "precio": "0.30",
        "disponible": true,
        "created": "2023-10-23T14:45:13.037276Z",
        "updated": "2023-10-23T15:18:18.138393Z"
    },
    {
        "id": 2,
        "nombre": "Aspirina",
        "fabricante": "Laboratorios Cofar",
        "pais_procedencia": "Bolivia",
        "unidades": "comp",
        "precio": "0.50",
        "disponible": true,
        "created": "2023-10-23T14:45:39.108791Z",
        "updated": "2023-10-23T15:17:33.164385Z"
    },
    etc, etc, etc...
]
```

## 9. Archivo Requirements.txt

El correpondiente archivo requirements.txt se encuentra en la raiz del proyecto