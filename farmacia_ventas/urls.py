from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(f"farmaceuticos", views.FarmaceuticoViewSet)
router.register(f"clientes", views.ClienteViewSet)
router.register(f"medicamentos", views.MedicamentoViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("farmaceuticos/cantidad/", views.farmaceuticos_cantidad, name="farmaceuticos_cantidad"),
    path("medicamentos/hechosen/bolivia/", views.medicamentos_hechosen_bolivia, name="medicamentos_hechosen_bolivia"),
    path("", include(router.urls)),
]