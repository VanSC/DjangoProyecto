from django.db import models

# Create your models here.
class Usuario(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombreusuario = models.CharField(max_length=40)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=80)
    email = models.EmailField(max_length=40)
    contraseña = models.CharField(max_length=12)

    def __str__(self):
        return self.nombreusuario

class Marca(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=500)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=60)
    stock=models.IntegerField()
    codigo_Modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    codigo_Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    codigo_Categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Orden_Ingreso(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    codigo_Articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cant_Art_Ingresados=models.IntegerField()
    fecha_Ingreso=models.DateTimeField()
    codigo_Usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo_Articulo

class Orden_Pedido(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    codigo_Articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cant_Solicitada=models.IntegerField()
    fecha_Solicitud=models.DateTimeField()
    codigo_Usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo_Articulo

class Orden_Salida(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    codigo_Articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cant_Art_Salida=models.IntegerField()
    fecha_Salida=models.DateTimeField()
    codigo_Usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo_Articulo

