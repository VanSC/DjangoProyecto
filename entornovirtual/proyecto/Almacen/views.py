from django.shortcuts import redirect, render
from .models import Usuario
from pyexpat.errors import messages

template_login="usuario/login.html"
template_registro = "usuario/registro.html"
template_index="producto/GestionProducto.html"
#"acciones/ingreso/edit_ingreso.html"
#"producto/lista_modelo.html"
#"base/index.html"
##validacion de usuario y registro

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['txtUsuario']
        password = request.POST['txtContraseña']
        
        user = Usuario.objects.get(nombreusuario=username,contraseña=password)
        
        if (user):
            context = {"msg":"usuario correcto","usuario":user}
            return render(request,template_index,context)
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
    

#Gestion a la tabla cursos
def index(request):
    return render(request,template_index)