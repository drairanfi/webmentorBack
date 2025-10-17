# WebMentor Backend

Backend API para WebMentor desarrollado con Django REST Framework.

## 🛠️ Tecnologías Utilizadas

- **Django 5.2.7** - Framework web de Python
- **Django REST Framework 3.16.1** - Toolkit para construir APIs REST
- **SQLite** - Base de datos (desarrollo) se genera automatico
- **JWT Authentication** - Autenticación mediante tokens JWT

## 📋 Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8+** 
- **pip** (gestor de paquetes de Python)
- **Git** 

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Webmentorback
```

### 2. Crear y activar un entorno virtual

**En Windows:**
```powershell
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

### 5. Crear un superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

## 📁 Estructura del Proyecto

```
Webmentorback/
│
├── configuration/          # Configuración principal de Django
│   ├── __init__.py
│   ├── settings.py        # Configuraciones del proyecto
│   ├── urls.py           # URLs principales
│   └── wsgi.py
│
├── login/                 # App de autenticación
│   ├── models.py         # Modelos de usuario
│   ├── serializers.py    # Serializadores DRF
│   ├── views.py          # Vistas de la API
│   ├── urls.py           # URLs del login
│   └── migrations/       # Migraciones de base de datos
│
├── manage.py             # Herramienta de gestión de Django
├── requirements.txt      # Dependencias del proyecto
├── db.sqlite3           # Base de datos SQLite (se genera automáticamente)
└── README.md            # Este archivo
```

## 🔐 Autenticación JWT

El proyecto utiliza JWT para autenticación. La configuración actual:

- **Access Token Lifetime**: 30 días
- **Refresh Token Lifetime**: 1 día
- **Header Type**: Bearer

### Endpoints de Autenticación

- `POST /webmentor/login/` - Iniciar sesión
- `POST /webmentor/register/` - Registrar usuario
- `POST /webmentor/token/refresh/` - Renovar token

Accede al panel de administración de Django en:
`http://127.0.0.1:8000/admin/`

## 📝 Comandos Útiles

```bash
# Ver todas las migraciones
python manage.py showmigrations

# Crear una nueva migración
python manage.py makemigrations nombre_app

# Aplicar una migración específica
python manage.py migrate nombre_app numero_migracion

# Abrir shell de Django
python manage.py shell

# Recolectar archivos estáticos (producción)
python manage.py collectstatic
```

## 🔄 Desarrollo

### Agregar nueva funcionalidad

1. Crear una nueva app Django:
   ```bash
   python manage.py startapp nombre_app
   ```

2. Agregar la app a `INSTALLED_APPS` en `settings.py`

3. Crear modelos, vistas, serializers según sea necesario

4. Crear y aplicar migraciones:
   ```bash
   python manage.py makemigrations nombre_app
   python manage.py migrate
   ```
