# Primera Página Web con Reflex
*Por Arianna Cedeño*

# Descripción:

Esta es una aplicación web interactiva de una sola página (SPA) desarrollada con Python utilizando el framework Reflex. Su propósito es demostrar cómo conectar una interfaz visual con lógica de programación en tiempo real mediante manejo de estado, sin necesidad de recargar la página ni usar JavaScript.

# ¿Qué hace la aplicación?

La aplicación permite al usuario interactuar con un botón que cambia dinámicamente el contenido y estilo de la página:

-Muestra un mensaje inicial de bienvenida

-Permite interactuar mediante un botón

-Cambia el texto y el color al hacer clic

-Permite alternar entre el estado inicial y el modificado


Todo esto ocurre de forma instantánea, sin recargas.

# Tecnologías utilizadas:
-Python 

-Reflex

-Visual Studio Code

-Poetry

-Node.js


# ¿Cómo funciona?
**-Pantalla inicial**
El usuario ve un título con el nombre del proyecto y un mensaje de bienvenida.

**-Mensaje central**
Se muestra una instrucción:
"¡Haz clic en el botón para ver la magia!"

**-Interacción**
Un botón permite al usuario interactuar con la aplicación.

**-Cambio dinámico**
Al hacer clic:
El texto cambia a un mensaje de éxito 🎉
El color del texto se vuelve más llamativo

**-Alternancia**
Si el usuario vuelve a hacer clic, el mensaje regresa a su estado original.

# ¿Cómo funciona internamente?

La aplicación utiliza una arquitectura reactiva basada en:

**-Estado (State):**
Guarda el texto y el color actuales.

**-Evento (interactuar):**
Función en Python que se ejecuta al hacer clic y modifica el estado.

**-Interfaz (UI):**
Se actualiza automáticamente cuando el estado cambia, sin recargar la página.

Esto permite una experiencia fluida y en tiempo real, como si la página “pensara” mientras el usuario interactúa.

##  Instrucciones para Ejecutar el Proyecto:

Sigue estos sencillos pasos en tu computadora para descargar y correr esta aplicación localmente:

### 1. Requisitos previos
Asegúrate de tener instalados en tu sistema:
* **Python** (versión 3.10 o superior)
* **Node.js** (versión 18.x o superior)
* **Poetry** (gestor de entornos y paquetes de Python)

### 2. Clonar el repositorio e instalar dependencias
Abre tu terminal y ejecuta los siguientes comandos:
```bash
# Clonar el proyecto
git clone https://github.com/AriAri2009/WebPageConReflex.git
cd WebPageConReflex

# Instalar Reflex y sus dependencias con Poetry
poetry install

# Inicializar la estructura de Reflex
poetry run reflex init



