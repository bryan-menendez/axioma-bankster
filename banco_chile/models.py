from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Cliente(models.Model):
    class Estados(models.TextChoices):
        ACTIVO = 'activo', _('Activo')
        INACTIVO = 'inactivo', _('Inactivo')
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=128)
    apellido_paterno = models.CharField(max_length=128)
    apellido_materno = models.CharField(max_length=128)
    saldo_contable = models.IntegerField(default=0)
    saldo_cta_corriente = models.IntegerField(default=0)
    saldo_linea_credito = models.IntegerField(default=0)
    total_cargos = models.IntegerField(default=0)
    total_abonos = models.IntegerField(default=0)
    estado = models.CharField(max_length=128, choices=Estados.choices, default=Estados.ACTIVO)

    def __str__(self):
        return str(self.user.id) + " - " + self.user.username + " - " + self.nombres + " " + self.apellido_paterno + " " + self.apellido_materno
