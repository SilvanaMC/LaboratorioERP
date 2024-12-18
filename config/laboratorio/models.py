from django.db import models


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255, db_index=True)
    ciudad = models.CharField(max_length=100, default='Temuco')  # Nuevo campo
    pais = models.CharField(max_length=100, default='Chile')    # Nuevo campo
    
    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    nueva_especialidad = models.CharField(max_length=100, default='General')
    
    def __str__(self):
        return f"{self.nombre} (Laboratorio: {self.laboratorio.nombre})"

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} (Laboratorio: {self.laboratorio.nombre})"
