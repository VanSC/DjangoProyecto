from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombreusuario = models.CharField(max_length=40)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=80)
    email = models.EmailField(max_length=40)
    contraseña = models.CharField(max_length=12)

