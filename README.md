# API de Arriendo de Estacionamientos

Bienvenido/a a la API de Arriendo de Estacionamientos. Esta API ha sido desarrollada utilizando Python y el framework Django para proporcionar una solución sencilla y eficiente para gestionar el arriendo de estacionamientos y la generación de contratos de arriendo.

## Características

- Registro y autenticación de administrador.
- Gestión de estacionamientos disponibles para arriendo.
- Creación de contrato de arriendo para el estacionamiento seleccionado.
- Califición de estacionamientos.
- Generación automática de contratos de arriendo en formato PDF.

## Requisitos de Instalación

1. Clona este repositorio: `git clone https://github.com/DiegoDonoso1/api-django.git`
2. Accede al directorio del proyecto
3. Crea un entorno virtual: `python -m venv venv`
4. Activa el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En macOS y Linux: `source venv/bin/activate`
5. Instala las dependencias: `pip install -r requisitos.txt`

## Configuración

1. Crea una base de datos y actualiza la configuración en `settings.py`.
2. Realiza las migraciones: `python manage.py migrate`
3. Crea un superusuario: `python manage.py createsuperuser`
4. Inicia el servidor: `python manage.py runserver`

## Uso

- Accede a la API en: `http://localhost:8000/api/{rutasDisponibles}`
- Utiliza herramientas como Postman para probar las rutas y funcionalidades.
- Para generar un contrato de arriendo, realiza una solicitud a la API correspondiente.







