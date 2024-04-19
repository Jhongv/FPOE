from django.db import models

class Cicla(models.Model):
    marca = models.TextField(max_length=50, null=False, blank=True)
    talla = models.TextField(max_length=5000, null=False, blank=True)
    componentes = models.CharField(max_length=50, null=False, blank=True, verbose_name="Componentes")
    valor = models.IntegerField(null=False, verbose_name="Valor")
    
    def __str__(self):
        return str(self.valor)
