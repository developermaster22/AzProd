# AzProd
# Sistema de Gestión de Pedidos - AZ Prod

**Descripción:**  
El Sistema de Gestión de Pedidos de AZ Paneles es una plataforma web desarrollada con **Django** para facilitar la gestión de pedidos en tiempo real. Permite a administradores y empleados gestionar pedidos, asignar tareas según el rol (diseñador, impresor, entelador, embolsador) y hacer seguimiento del estado de cada pedido desde cualquier dispositivo.

## Características

- Gestión de pedidos por estado
- Asignación de tareas a los diferentes roles (diseñador, impresor, etc.)
- Panel de administración para crear y gestionar usuarios
- Interfaz amigable, optimizada para tablets y dispositivos móviles
- Registro y login de usuarios con roles personalizados

## Tecnologías utilizadas

- **Python 3.x**
- **Django 5.x**
- **HTML5, CSS3, Bootstrap** para la interfaz
- **SQLite** (base de datos por defecto)

## Instalación

### Requisitos previos

1. **Python 3.x**: Asegúrate de tener instalado Python 3. Si no lo tienes, puedes descargarlo desde [python.org](https://www.python.org/).
2. **pip**: El administrador de paquetes de Python, para instalar dependencias.

### Pasos para instalar el proyecto

1. **Clona el repositorio:**
   
   ```bash
   git clone https://github.com/tu-usuario/az-paneles.git
   cd az-paneles
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Aplica las migraciones de la base de datos:

bash
Copiar
Editar
python manage.py migrate
Crea un superusuario para acceder al panel de administración:

bash
Copiar
Editar
python manage.py createsuperuser
Inicia el servidor de desarrollo:

bash
Copiar
Editar
python manage.py runserver
Abre tu navegador y ve a http://127.0.0.1:8000/pedidos/ para acceder al sistema.

Acceder al panel de administración
Inicia sesión con el superusuario creado en el paso anterior. Esto te permitirá gestionar usuarios y ver los pedidos.

Estructura del proyecto
pgsql
Copiar
Editar
az_paneles/
│
├── pedidos/
│   ├── migrations/
│   ├── templates/
│   │   ├── pedidos/
│   │   │   ├── admin.html
│   │   │   └── lista.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── db.sqlite3

#Contribuir
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

Haz un fork del proyecto.

Crea una nueva rama (git checkout -b nueva-funcionalidad).

Realiza los cambios y haz commit de los mismos (git commit -am 'Añadí nueva funcionalidad').

Haz push a la rama (git push origin nueva-funcionalidad).

Abre un Pull Request.

Licencia
Este proyecto está bajo la licencia MIT - ver el archivo LICENSE para más detalles.

¡Gracias por usar AZ Prod! 😊
