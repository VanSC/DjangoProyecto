from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Usuario, Marca, Modelo, Categoria, Articulo, Orden_Ingreso, Orden_Pedido, Orden_Salida
from pyexpat.errors import messages
from django.db.models import Avg, Max, Count, Sum, Q, F

template_login="usuario/login.html"
template_registro = "usuario/registro.html"
#template_index="inicio.html"
##VISTAS

#Acciones
#acciones/ingreso/GestionIngreso.html
#acciones/ingreso/edit_ingreso.html

#acciones/pedido/GestionPedido.html
#acciones/pedido/edit_pedido.html

#acciones/pedido/GestionSalida.html
#acciones/pedido/edit_salida.html

##Productos 
template_gestion_articulo="articulo/GestionArticulo.html"
template_edit_articulo="articulo/edit_articulo.html"
#producto/GestionProducto.html
#producto/edit_producto.html

### Categoria
template_gestion_categoria="articulo/categoria/GestionCategoria.html"
template_edit_categoria="articulo/categoria/edit_categoria.html"
#producto/categoria/GestionCategoria.html
#producto/categoria/editCategoria.html

### Marca
template_gestion_marca="articulo/marca/GestionMarca.html"
template_edit_marca="articulo/marca/edit_marca.html"
#producto/marca/GestionMarca.html
#producto/marca/edit_marca.html

### Modelo
template_gestion_modelo="articulo/modelo/GestionModelo.html"
template_edit_modelo="articulo/modelo/edit_modelo.html"
#producto/modelo/GestionModelo.html
#producto/modelo/edit_modelo.html

### Reporte de ingresos
template_reporte_ingresos="reportes/reporteingreso.html"
#producto/modelo/GestionModelo.html
#producto/modelo/edit_modelo.html

### Reporte de pedido
template_reporte_pedidos="reportes/reportePedido.html"

### Reporte de salida
template_reporte_salidas="reportes/reporteSalida.html"


##validacion de usuario y registro
"""
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['txtUsuario']
        password = request.POST['txtContraseña']
        
        user = Usuario.objects.get(nombreusuario=username,contraseña=password)
        articulos = Articulo.objects.all()
        modelos = Modelo.objects.all()
        marcas = Marca.objects.all()
        categorias = Categoria.objects.all()
        
        if (user):
            context = {"msg":"usuario correcto","usuario":user,"articulos":articulos,"modelos":modelos,"marcas":marcas,"categorias":categorias}
            return render(request,template_gestion_articulo,context)
        else:
            message = {"msg":"datos invalidos"}
            return render(request,template_login,message)
    else:
        return render(request,template_login)    
    
    
#registro usuario
def registrar_usuario(request):
    if request.method == 'POST':
        codigo = request.POST["txtCodigo"]
        username = request.POST["txtUsuario"]
        name = request.POST["txtNombre"]
        lastname = request.POST["txtApellido"]
        email = request.POST["txtEmail"]
        password1 = request.POST["txtPass1"]
        password2 = request.POST["txtPass2"]

        if password1==password2:
            if Usuario.objects.filter(nombreusuario=username).exists():
                message = {"msg":"usuario existe"}
                return render(request,template_registro,message)
            else:
                user = Usuario.objects.create(codigo=codigo,nombreusuario=username,nombre=name,apellido=lastname,email=email,contraseña=password1)
                user.save()
                context = {"msg":"usuario correcto"}
                return render(request,template_login,context)
        else:
            messages.info(request,'las contraseña no coinciden')
            return redirect('/registro')
    else:
        return render(request,template_registro)
"""    

#Gestion a la tabla marca

def salir(request):
    logout(request)
    return redirect('/')

@login_required
def marca(request):
    marcas = Marca.objects.all()
    context = {"marcas":marcas}
    return render(request, template_gestion_marca,context)

@login_required
def edicionmarca(request, codigo):
    marca = Marca.objects.get(codigo = codigo)
    context = {"marca":marca}
    return render(request, template_edit_marca,context)

@login_required
def updatemarca(request, codigo):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]

    marca = Marca.objects.get(codigo = codigo)
    marca.codigo = codigo
    marca.nombre = nombre
    marca.save()
    return redirect("/marca")

@login_required
def registrarmarca(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]

    marca = Marca.objects.create(codigo=codigo,nombre=nombre)
    return redirect("/marca")

@login_required
def eliminarmarca(request, codigo):
    marca = Marca.objects.get(codigo = codigo)
    marca.delete()
    return redirect("/marca")


#Gestion a la tabla modelo
@login_required
def modelo(request):
    modelos = Modelo.objects.all()
    context = {"modelos":modelos}
    return render(request, template_gestion_modelo,context)

@login_required
def edicionmodelo(request, codigo):
    modelo = Modelo.objects.get(codigo = codigo)
    context = {"modelo":modelo}
    return render(request, template_edit_modelo,context)

@login_required
def updatemodelo(request, codigo):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]

    modelo = Modelo.objects.get(codigo = codigo)
    modelo.codigo = codigo
    modelo.nombre = nombre
    modelo.save()
    return redirect("/modelo")

@login_required
def registrarmodelo(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]

    modelo = Modelo.objects.create(codigo=codigo,nombre=nombre)
    return redirect("/modelo")

@login_required
def eliminarmodelo(request, codigo):
    modelo = Modelo.objects.get(codigo = codigo)
    modelo.delete()
    return redirect("/modelo")


#Gestion a la tabla categoria
@login_required
def categoria(request):
    categorias = Categoria.objects.all()
    context = {"categorias":categorias}
    return render(request, template_gestion_categoria,context)

@login_required
def edicioncategoria(request, codigo):
    categoria = Categoria.objects.get(codigo = codigo)
    context = {"categoria":categoria}
    return render(request, template_edit_categoria,context)

@login_required
def updatecategoria(request, codigo):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    descripcion = request.POST["txtDescripcion"]

    categoria = Categoria.objects.get(codigo = codigo)
    categoria.codigo = codigo
    categoria.nombre = nombre
    categoria.descripcion = descripcion
    categoria.save()
    return redirect("/categoria")

@login_required
def registrarcategoria(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    descripcion = request.POST["txtDescripcion"]

    categoria = Categoria.objects.create(codigo=codigo,nombre=nombre,descripcion=descripcion)
    return redirect("/categoria")

@login_required
def eliminarcategoria(request, codigo):
    categoria = Categoria.objects.get(codigo = codigo)
    categoria.delete()
    return redirect("/categoria")


#Gestion a la tabla articulo
@login_required
def articulo(request):
    articulos = Articulo.objects.all()
    modelos = Modelo.objects.all()
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    context = {"articulos":articulos,"modelos":modelos,"marcas":marcas,"categorias":categorias}
    return render(request, template_gestion_articulo,context)

@login_required
def edicionarticulo(request, codigo):
    articulo = Articulo.objects.get(codigo = codigo)
    modelos = Modelo.objects.all()
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    context = {"articulo":articulo,"modelos":modelos,"marcas":marcas,"categorias":categorias}
    return render(request, template_edit_articulo,context)

@login_required
def updatearticulo(request, codigo):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    stock = request.POST["txtStock"]
    modelo = request.POST["txtModelo"]
    marca = request.POST["txtMarca"]
    categoria = request.POST["txtCategoria"]

    articulo = Articulo.objects.get(codigo = codigo)
    articulo.codigo = codigo
    articulo.nombre = nombre
    articulo.stock = stock
    modelo_fk = Modelo.objects.get(codigo = modelo)
    articulo.codigo_Modelo = modelo_fk
    marca_fk = Marca.objects.get(codigo = marca)
    articulo.codigo_Marca = marca_fk
    categoria_fk = Categoria.objects.get(codigo = categoria)
    articulo.codigo_Categoria = categoria_fk

    articulo.save()
    return redirect("/articulo")


@login_required
def registrararticulo(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    stock = request.POST["txtStock"]
    modelo = request.POST["txtModelo"]
    marca = request.POST["txtMarca"]
    categoria = request.POST["txtCategoria"]

    modelo_fk = Modelo.objects.get(codigo = modelo)
    marca_fk = Marca.objects.get(codigo = marca)
    categoria_fk = Categoria.objects.get(codigo = categoria)

    articulo = Articulo.objects.create(codigo=codigo,nombre=nombre,stock=stock,codigo_Modelo=modelo_fk,codigo_Marca=marca_fk,codigo_Categoria=categoria_fk)
    #articulo.save()
    return redirect("/articulo")

@login_required
def eliminararticulo(request, codigo):
    articulo = Articulo.objects.get(codigo = codigo)
    articulo.delete()
    return redirect("/articulo")


### 

template_gestion_ingreso="acciones/ingreso/GestionIngreso.html"
template_edit_ingreso="acciones/ingreso/edit_ingreso.html"

template_gestion_pedido="acciones/pedido/GestionPedido.html"
template_edit_pedido="acciones/pedido/edit_pedido.html"

#Gestion a la tabla ingreso
@login_required
def ingreso(request):
    ingresos = Orden_Ingreso.objects.all()
    articulos = Articulo.objects.all()
    usuarios = Usuario.objects.all()
    context = {"ingresos":ingresos, "articulos":articulos, "usuarios":usuarios}
    return render(request, template_gestion_ingreso,context)

@login_required
def edicioningreso(request, codigo):
    ingreso = Orden_Ingreso.objects.get(codigo = codigo)
    articulos = Articulo.objects.all()
    usuarios = Usuario.objects.all()
    context = {"ingreso":ingreso, "articulos":articulos, "usuarios":usuarios}
    return render(request, template_edit_ingreso, context)

@login_required
def updateingreso(request, codigo):
    codigo = request.POST["txtCodigo"]
    articulo = request.POST["txtArticulo"]
    cantidad = request.POST["txtCantidad"]
    fecha = request.POST["txtFecha"]
    hora = request.POST["txtHora"]
    usuario =  request.POST["txtUsuario"]

    ingreso = Orden_Ingreso.objects.get(codigo = codigo)

    articulo_fk = Articulo.objects.get(codigo = articulo)
    ingreso.codigo_Articulo = articulo_fk
    usuario_fk = Usuario.objects.get(codigo = usuario)
    ingreso.codigo_Usuario = usuario_fk

    ingreso.cant_Art_Ingresados = cantidad
    ingreso.save()
    return redirect("/ingreso")

@login_required
def registraringreso(request):
    codigo = request.POST["txtCodigo"]
    articulo = request.POST["txtArticulo"]
    cantidad = request.POST["txtCantidad"]
    fecha = request.POST["txtFecha"]
    hora = request.POST["txtHora"]
    usuario =  request.POST["txtUsuario"]

    articulo_fk = Articulo.objects.get(codigo = articulo)
    usuario_fk = Usuario.objects.get(codigo = usuario)

    ingreso = Orden_Ingreso.objects.create(codigo=codigo,codigo_Articulo=articulo_fk,cant_Art_Ingresados=cantidad,fecha_Ingreso=fecha,hora_Ingreso=hora,codigo_Usuario=usuario_fk)
    
    ## prueba de transaccion de ingreso
    trans_stock = articulo_fk.stock + int(cantidad)
    articulo_fk.stock = trans_stock
    articulo_fk.save() 
    ##

    return redirect("/ingreso")

@login_required
def eliminaringreso(request, codigo):
    ingreso = Orden_Ingreso.objects.get(codigo = codigo)
    ingreso.delete()
    return redirect("/ingreso")



#Gestion a la tabla Pedido
@login_required
def pedido(request):
    pedidos = Orden_Pedido.objects.all()
    articulos = Articulo.objects.all()
    usuarios = Usuario.objects.all()
    context = {"pedidos":pedidos, "articulos":articulos, "usuarios":usuarios}
    return render(request, template_gestion_pedido,context)

@login_required
def edicionpedido(request, codigo):
    pedido = Orden_Pedido.objects.get(codigo = codigo)
    context = {"pedido":pedido}
    return render(request, template_edit_pedido, context)

@login_required
def updatepedido(request, codigo):
    codigo = request.POST["txtCodigo"]
    articulo = request.POST["txtArticulo"]
    cantidad = request.POST["txtCantidad"]
    fecha = request.POST["txtFecha"]
    hora = request.POST["txtHora"]
    usuario =  request.POST["txtUsuario"]

    pedido = Orden_Pedido.objects.get(codigo = codigo)

    articulo_fk = Articulo.objects.get(codigo = articulo)
    pedido.codigo_Articulo = articulo_fk
    usuario_fk = Usuario.objects.get(codigo = usuario)
    pedido.codigo_Usuario = usuario_fk

    pedido.cant_Solicitada = cantidad

    pedido.save()
    return redirect("/pedido")

@login_required
def registrarpedido(request):
    codigo = request.POST["txtCodigo"]
    articulo = request.POST["txtArticulo"]
    cantidad = request.POST["txtCantidad"]
    fecha = request.POST["txtFecha"]
    hora = request.POST["txtHora"]
    usuario =  request.POST["txtUsuario"]

    articulo_fk = Articulo.objects.get(codigo = articulo)
    usuario_fk = Usuario.objects.get(codigo = usuario)

    pedido = Orden_Pedido.objects.create(codigo=codigo,codigo_Articulo=articulo_fk,cant_Solicitada=cantidad,fecha_Solicitud=fecha,hora_Solicitud=hora,codigo_Usuario=usuario_fk)
    return redirect("/pedido")

@login_required
def eliminarpedido(request, codigo):
    pedido = Orden_Pedido.objects.get(codigo = codigo)
    pedido.delete()
    return redirect("/pedido")

#Gestion a la tabla Salida
template_gestion_salida="acciones/salida/GestionSalida.html"
template_edit_salida="acciones/salida/edit_salida.html"

@login_required
def salida(request):
    salidas = Orden_Salida.objects.all()
    articulos = Articulo.objects.all()
    usuarios = Usuario.objects.all()
    context = {"salidas":salidas, "articulos":articulos, "usuarios":usuarios}
    return render(request, template_gestion_salida, context)

@login_required
def edicionsalida(request, codigo):
    salida = Orden_Salida.objects.get(codigo = codigo)
    context = {"salida":salida}
    return render(request, template_edit_salida, context)

@login_required
def updatesalida(request, codigo):
    codigo = request.POST["txtCodigo"]
    articulo = request.POST["txtArticulo"]
    cantidad = request.POST["txtCantidad"]
    fecha = request.POST["txtFecha"]
    hora = request.POST["txtHora"]
    usuario =  request.POST["txtUsuario"]

    salida = Orden_Salida.objects.get(codigo = codigo)

    articulo_fk = Articulo.objects.get(codigo = articulo)
    salida.codigo_Articulo = articulo_fk
    usuario_fk = Usuario.objects.get(codigo = usuario)
    salida.codigo_Usuario = usuario_fk

    salida.cant_Art_Salida = cantidad

    salida.save()
    return redirect("/salida")

@login_required
def registrarsalida(request):
    codigo = request.POST["txtCodigo"]
    articulo = request.POST["txtArticulo"]
    cantidad = request.POST["txtCantidad"]
    fecha = request.POST["txtFecha"]
    hora = request.POST["txtHora"]
    usuario =  request.POST["txtUsuario"]

    articulo_fk = Articulo.objects.get(codigo = articulo)
    usuario_fk = Usuario.objects.get(codigo = usuario)

        
    ## prueba de transaccion de salida
    trans_stock = articulo_fk.stock - int(cantidad)
    if(trans_stock >= 0):
        salida = Orden_Salida.objects.create(codigo=codigo,codigo_Articulo=articulo_fk,cant_Art_Salida=cantidad,fecha_Salida=fecha,hora_Salida=hora,codigo_Usuario=usuario_fk)
        articulo_fk.stock = trans_stock
        articulo_fk.save() 
    ##
    

    return redirect("/salida")

@login_required
def eliminarsalida(request, codigo):
    salida = Orden_Salida.objects.get(codigo = codigo)
    salida.delete()
    return redirect("/salida")



## consultas para reportes
@login_required
def reporteingreso(request):
    fingreso = request.POST.get("txtfingreso")
    #reporte = Orden_Ingreso.objects.values('codigo_Articulo','codigo_Articulo__nombre').annotate(cantidad=Sum('cant_Art_Ingresados')).order_by('-cantidad')
    reporte = Articulo.objects.annotate(value=Sum(F('orden_ingreso__cant_Art_Ingresados'))).values('codigo','nombre','value').order_by('-value')

    if fingreso:
        reporte = Articulo.objects.annotate(value=Sum(F('orden_ingreso__cant_Art_Ingresados'))).values('codigo','nombre','value').order_by('-value').filter(orden_ingreso__fecha_Ingreso__month = fingreso).distinct()
        #reporte = Articulo.objects.annotate(value=Sum(F('orden_ingreso__cant_Art_Ingresados'))).values('codigo','nombre','value').order_by('-value').filter(orden_ingreso__fecha_Ingreso__month='07') 
    
    context = {"reporte":reporte}
    return render(request, template_reporte_ingresos, context)   


@login_required
def reportepedido(request):
    fpedido = request.POST.get("txtfpedido")
    #reporte = Orden_Ingreso.objects.values('codigo_Articulo','codigo_Articulo__nombre').annotate(cantidad=Sum('cant_Art_Ingresados')).order_by('-cantidad')
    reporte = Articulo.objects.annotate(value=Sum(F('orden_pedido__cant_Solicitada'))).values('codigo','nombre','value').order_by('-value')
    
    if fpedido:
        reporte = Articulo.objects.annotate(value=Sum(F('orden_pedido__cant_Solicitada'))).values('codigo','nombre','value').order_by('-value').filter(orden_pedido__fecha_Solicitud__month = fpedido).distinct()
    
    context = {"reporte":reporte}
    return render(request, template_reporte_pedidos, context)


@login_required
def reportesalida(request):
    fsalida = request.POST.get("txtfsalida")
    #reporte = Orden_Ingreso.objects.values('codigo_Articulo','codigo_Articulo__nombre').annotate(cantidad=Sum('cant_Art_Ingresados')).order_by('-cantidad')
    reporte = Articulo.objects.annotate(value=Sum(F('orden_salida__cant_Art_Salida'))).values('codigo','nombre','value').order_by('-value')
    
    if fsalida:
        reporte = Articulo.objects.annotate(value=Sum(F('orden_salida__cant_Art_Salida'))).values('codigo','nombre','value').order_by('-value').filter(orden_salida__fecha_Salida__month = fsalida).distinct()
    
    
    context = {"reporte":reporte}
    return render(request, template_reporte_salidas, context)
