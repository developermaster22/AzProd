from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Pedido, UsuarioPersonalizado
from .forms import CustomUserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import User


# Vista de lista de pedidos
@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.all()  # Obtiene todos los pedidos
    return render(request, 'pedidos/lista.html', {'pedidos': pedidos})

# Vista de login
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print(f"Usuario autenticado: {user.username}")
            print(f"Rol del usuario: {user.rol}")  # Verifica el rol del usuario
            
            login(request, user)
            
            # Redirigir al panel según el rol del usuario
            if user.rol == 'diseñador':
                return redirect('panel_disenador')
            elif user.rol == 'impresor':
                return redirect('panel_impresor')
            elif user.rol == 'entelador':
                return redirect('panel_entelador')
            elif user.rol == 'embolsador':
                return redirect('panel_embolsador')
            elif user.rol == 'admin':
                return redirect('panel_admin')
            else:
                return HttpResponse('Rol de usuario no reconocido.')
        else:
            print(f"Credenciales inválidas para {username}")
            return HttpResponse('Credenciales inválidas. Inténtalo de nuevo.')
    return render(request, 'pedidos/login.html')


# Paneles por rol
@login_required
def panel_disenador(request):
    return render(request, 'pedidos/disenador.html')

@login_required
def panel_impresor(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/impresor.html', {'pedidos': pedidos})

@login_required
def ver_pedido_impresion(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedidos/ver_pedido_impresion.html', {'pedido': pedido})

@login_required
def panel_entelador(request):
    return render(request, 'pedidos/entelador.html')

@login_required
def panel_embolsador(request):
    return render(request, 'pedidos/embolsador.html')

# Panel del Administrador

@login_required
def panel_admin(request):
    # Obtener todos los usuarios usando el modelo personalizado
    usuarios = UsuarioPersonalizado.objects.all()  # Correcto si estás usando el modelo personalizado
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/admin.html', {'usuarios': usuarios, 'pedidos': pedidos})


# Crear usuario
@login_required
def crear_usuario(request):
    if request.user.is_superuser:  # Aseguramos que solo el admin pueda crear usuarios
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()  # Guarda el nuevo usuario
                return redirect('lista_usuarios')  # Redirigir a una vista de lista de usuarios o donde desees
        else:
            form = CustomUserCreationForm()

        return render(request, 'pedidos/crear_usuario.html', {'form': form})
    else:
        return redirect('lista_pedidos')  # Si no es admin, redirigir a lista de pedidos

# Vista de la lista de usuarios
@login_required
def lista_usuarios(request):
    # Obtener todos los usuarios usando el modelo personalizado
    usuarios = UsuarioPersonalizado.objects.all()
    return render(request, 'pedidos/lista_usuarios.html', {'usuarios': usuarios})

# Vista de inicio de pedidos
@login_required
def pedidos_home(request):
    return render(request, 'pedidos/home.html')



@login_required
def editar_usuario(request, usuario_id):
    if request.user.is_superuser:
        usuario = get_object_or_404(User, id=usuario_id)  # Obtén el usuario por ID
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                return redirect('lista_usuarios')
        else:
            form = CustomUserChangeForm(instance=usuario)
        return render(request, 'pedidos/editar_usuario.html', {'form': form, 'usuario': usuario})
    else:
        return redirect('panel_admin')  # Si no es admin, redirigir al panel de admin
    # Vista para eliminar usuario
@login_required
def eliminar_usuario(request, user_id):
    usuario = get_object_or_404(UsuarioPersonalizado, id=user_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')  # Redirigir a lista de usuarios
    return render(request, 'pedidos/eliminar_usuario.html', {'usuario': usuario})