import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Pedido(models.Model):
    codigo = models.CharField(max_length=12, unique=True, editable=False)
    diseño = models.ImageField(upload_to='diseños/')
    impresion_realizada = models.BooleanField(default=False)
    entelado_realizado = models.BooleanField(default=False)
    embolsado_realizado = models.BooleanField(default=False)
    foto_final = models.ImageField(upload_to='finales/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = str(uuid.uuid4())[:12].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido {self.codigo}"


class UsuarioPersonalizado(AbstractUser):
    ROLES = [
        ('diseñador', 'Diseñador'),
        ('impresor', 'Impresor'),
        ('entelador', 'Entelador'),
        ('embolsador', 'Embolsador'),
        ('admin', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES)