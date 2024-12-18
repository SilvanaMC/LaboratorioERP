from django.urls import path
from . import views

app_name = 'laboratorio'  # Asegúrate de que este namespace se use en tus pruebas

urlpatterns = [
    path('', views.lista_laboratorios, name='lista_laboratorios'),
    path('<int:id>/', views.detalle_laboratorio, name='detalle_laboratorio'),
    path('nuevo/', views.nuevo_laboratorio, name='nuevo_laboratorio'),
    path('<int:id>/editar/', views.editar_laboratorio, name='editar_laboratorio'),
    path('<int:id>/eliminar/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]
