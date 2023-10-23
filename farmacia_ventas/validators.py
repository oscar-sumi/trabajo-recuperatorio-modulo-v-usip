from django.core.exceptions import ValidationError

def validation_nombre_farmaceutico(value):
    if value == "admin":
        raise ValidationError("No esta permitido usar la palabra admin como nombre")
    
def validation_nombre_cliente(value):
    if value == "cliente":
        raise ValidationError("No esta permitido usar la palabra cliente como nombre")
    
def validacion_precio_medicamento(value):
    if value == 0:
        raise ValidationError(f"El precio del medicamento no puede ser 0")