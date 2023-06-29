from django.shortcuts import redirect, render
from .models import Usuario, Marca, Modelo, Categoria, Articulo, Orden_Ingreso, Orden_Pedido, Orden_Salida
from pyexpat.errors import messages

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
template_gestion_articulo="producto/GestionProducto.html"
template_edit_articulo="producto/GestionProducto.html"
#producto/GestionProducto.html
#producto/edit_producto.html

### Categoria
template_gestion_categoria="producto/GestionCategoria.html"
template_edit_categoria="producto/categoria/edit_categoria.html"
#producto/categoria/GestionCategoria.html
#producto/categoria/editCategoria.html

### Marca
template_gestion_marca="producto/GestionMarca.html"
template_edit_marca="producto/edit_marca.html"
#producto/marca/GestionMarca.html
#producto/marca/edit_marca.html

### Modelo
template_gestion_modelo="producto/modelo/GestionModelo.html"
template_edit_modelo="producto/modelo/edit_modelo.html"
#producto/modelo/GestionModelo.html
#producto/modelo/edit_modelo.html



##validacion de usuario y registro

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['txtUsuario']
        password = request.POST['txtContraseña']
        
        user = Usuario.objects.get(nombreusuario=username,contraseña=password)
        
        if (user):
            context = {"msg":"usuario correcto","usuario":user}
            return render(request,template_gestion_articulo,context)
        else:
            message = {"msg":"datos invalidos"}
            return render(request,template_login,message)
    else:
        return render(request,template_login)    
    
    
#registro usuario
def registrar_usuario(request):
    if request.method == 'POST':
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
                user = Usuario.objects.create(nombreusuario=username,nombre=name,apellido=lastname,email=email,contraseña=password1)
                user.save()
                context = {"msg":"usuario correcto"}
                return render(request,template_login,context)
        else:
            messages.info(request,'las contraseña no coinciden')
            return redirect('/registro')
    else:
        return render(request,template_registro)
    

#Gestion a la tabla marca
def marca(request):
    marcas = Marca.objects.all()
    context = {"marcas":marcas}
    return render(request, template_gestion_marca,context)

def edicionmarca(request, codigo):
    marca = Marca.objects.get(codigo = codigo)
    context = {"marca":marca}
    return render(request, template_edit_marca,context)

def updatemarca(request, codigo):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]

    marca = Marca.objects.get(codigo = codigo)
    marca.codigo = codigo
    marca.nombre = nombre
    marca.save()
    return redirect("/marca")

def registrarmarca(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]

    marca = Marca.objects.create(codigo=codigo,nombre=nombre)
    return redirect("/marca")

def eliminarmarca(request, codigo):
    marca = Marca.objects.get(codigo = codigo)
    marca.delete()
    return redirect("/marca")


#Gestion a la tabla modelo
def modelo(request):
    modelos = Modelo.objects.all()
    context = {"modelos":modelos}
    return render(request, template_gestion_modelo,context)

def edicionmodelo(request, codigo):
    modelo = Modelo.objects.get(codigo = codigo)
    context = {"modelo":modelo}
    return render(request, template_edit_modelo,context)

def updatemodelo(request, codigo):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]

    modelo = Modelo.objects.get(codigo = codigo)
    modelo.codigo = codigo
    modelo.nombre = nombre
    modelo.save()
    return redirect("/modelo")

def registrarmodelo(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]

    modelo = Modelo.objects.create(codigo=codigo,nombre=nombre)
    return redirect("/modelo")

def eliminarmodelo(request, codigo):
    modelo = Modelo.objects.get(codigo = codigo)
    modelo.delete()
    return redirect("/modelo")


#Gestion a la tabla categoria
def categoria(request):
    categorias = Categoria.objects.all()
    context = {"categorias":categorias}
    return render(request, template_gestion_categoria,context)

def edicioncategoria(request, codigo):
    categoria = Categoria.objects.get(codigo = codigo)
    context = {"categoria":categoria}
    return render(request, template_edit_categoria,context)

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

def registrarcategoria(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    descripcion = request.POST["txtDescripcion"]

    categoria = Categoria.objects.create(codigo=codigo,nombre=nombre,descripcion=descripcion)
    return redirect("/categoria")

def eliminarcategoria(request, codigo):
    categoria = Categoria.objects.get(codigo = codigo)
    categoria.delete()
    return redirect("/categoria")


#Gestion a la tabla articulo
def articulo(request):
    articulos = Articulo.objects.all()
    context = {"articulos":articulos}
    return render(request, template_gestion_articulo,context)

def edicionarticulo(request, codigo):
    articulo = Articulo.objects.get(codigo = codigo)
    context = {"articulo":articulo}
    return render(request, template_edit_articulo,context)

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
    articulo.modelo = modelo_fk
    marca_fk = Marca.objects.get(codigo = marca)
    articulo.marca = marca_fk
    categoria_fk = Categoria.objects.get(codigo = categoria)
    articulo.categoria = categoria_fk

    articulo.save()
    return redirect("/articulo")


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

    articulo = Articulo.objects.create(codigo=codigo,nombre=nombre,stock=stock,modelo=modelo_fk,marca=marca_fk,categoria=categoria_fk)
    return redirect("/articulo")

def eliminararticulo(request, codigo):
    articulo = Articulo.objects.get(codigo = codigo)
    articulo.delete()
    return redirect("/articulo")
