from django.contrib import admin
from .models import Usuario, Categoria, Articulo, Marca, Modelo, Orden_Salida, Orden_Ingreso, Orden_Pedido

##user admin
##pass admin

class AdminUsuario(admin.ModelAdmin):
    list_display=("codigo","nombreusuario","nombre","apellido","email","contraseña")

class AdminMarca(admin.ModelAdmin):
    list_display=('codigo','nombre')

class AdminModelo(admin.ModelAdmin):
    list_display=('codigo','nombre')

class AdminCategoria(admin.ModelAdmin):
    list_display=('codigo','nombre','descripcion')

class AdminArticulo(admin.ModelAdmin):
    list_display=('codigo','nombre','stock','codigo_Modelo','codigo_Marca','codigo_Categoria')

class AdminOrdenIngreso(admin.ModelAdmin):
    list_display=('codigo','codigo_Articulo','cant_Art_Ingresados','fecha_Ingreso','codigo_Usuario')

class AdminOrdenPedido(admin.ModelAdmin):
    list_display=('codigo','codigo_Articulo','cant_Solicitada','fecha_Solicitud','codigo_Usuario')

class AdminOrdenSalida(admin.ModelAdmin):
    list_display=('codigo','codigo_Articulo','cant_Art_Salida','fecha_Salida','codigo_Usuario')

admin.site.register(Usuario,AdminUsuario)
admin.site.register(Categoria,AdminCategoria)
admin.site.register(Articulo,AdminArticulo)
admin.site.register(Marca,AdminMarca)
admin.site.register(Modelo,AdminModelo)
admin.site.register(Orden_Ingreso,AdminOrdenIngreso)
admin.site.register(Orden_Pedido,AdminOrdenPedido)
admin.site.register(Orden_Salida,AdminOrdenSalida)



