#README - Proyecto de Automatización QA 
##1. Propósito del Proyecto
El objetivo de esta pre-entrega es aplicar conocimientos de Selenium WebDriver y Python para automatizar flujos básicos en la web saucedemo.com.

##2. Tecnologías Requeridas
- Python
- Pytest (estructura de testing)
- Selenium WebDriver (automatización)
- Git y GitHub (control de versiones)

##3. Estructura del Proyecto
- tests/: Archivos de prueba (ej. test_saucedemo.py).
- utils/: Funciones auxiliares y configuración del driver.
- reports/: Reportes HTML generados.
- datos/: Datos externos (si aplica).

##4. Instrucciones de Instalación
   1. Clonar el repositorio.
   2. Crear un entorno virtual: python -m venv venv
   3. Activar el entorno:
      - Windows: venv\Scripts\activate
      - Mac/Linux: source venv/bin/activate
   4. Instalar dependencias: pip install selenium pytest pytest-html

##5. Cómo ejecutar las pruebas
Para correr los tests y generar el reporte HTML, usa el comando:
pytest --html=reports/reporte.html --self-contained-html

##6. Casos de Prueba Incluidos
- Automatización de Login (credenciales válidas).
- Navegación y Verificación del Catálogo (título y productos).
- Interacción con Carrito (añadir producto y verificar contador).
