from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),  # Página principal
    path('login/', views.login_view, name='login_view'),  # Ruta de login
    path('panel_disenador/', views.panel_disenador, name='panel_disenador'),
    path('panel_impresor/', views.panel_impresor, name='panel_impresor'),
    path('ver_pedido_impresion/<int:pedido_id>/', views.ver_pedido_impresion, name='ver_pedido_impresion'),
    path('panel_entelador/', views.panel_entelador, name='panel_entelador'),
    path('panel_embolsador/', views.panel_embolsador, name='panel_embolsador'),
    path('panel_admin/', views.panel_admin, name='panel_admin'),
    path('home/', views.pedidos_home, name='pedidos_home'),
    path('lista/', views.lista_pedidos, name='lista_pedidos'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
     path('eliminar_usuario/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
     path('editar_usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),  # Nueva ruta para editar usuario
]
