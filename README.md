# Primera Página Web con Reflex
*Por Arianna Cedeño*

# Descripción:

Esta aplicación es una página web interactiva de una sola página (SPA) desarrollada en Python utilizando el framework Reflex.

El proyecto implementa un sistema de interacción cíclica donde el usuario recibe frases motivacionales dinámicas al presionar un botón, creando una experiencia continua basada en el manejo de estado.

# ¿Qué hace la aplicación?

La aplicación permite al usuario interactuar con un botón que cambia dinámicamente el contenido y estilo de la página:

-Muestra un mensaje inicial invitando a interactuar

-Al hacer clic, presenta una frase motivacional con colores llamativos

-Alterna entre invitación y recompensa en cada clic

-Recorre una secuencia de frases

-Se reinicia automáticamente al finalizar el ciclo

El usuario puede interactuar indefinidamente, generando una experiencia dinámica y repetible.

# Tecnologías utilizadas:
-Python 

-Reflex

-Visual Studio Code

-Poetry

-Node.js


# ¿Cómo funciona?
**-Pantalla inicial**

El usuario ve el título del proyecto junto a un diseño personalizado con una imagen de fondo y un contenedor central donde aparecerán los mensajes.

**-Mensaje central**

Se muestra una instrucción inicial:
"¡Haz clic en el botón para ver la magia!"
Este mensaje aparece en un color neutro, indicando que el sistema está en espera.

**-Interacción**

El usuario puede presionar el botón para comenzar la experiencia interactiva.

**-Cambio dinámico**

Al hacer clic:
Se muestra una frase motivacional diferente 
El color del texto cambia a un tono más llamativo (azul, naranja, índigo o púrpura)

**-Flujo continuo**

Cada vez que el usuario hace clic, el sistema avanza a la siguiente frase de la lista.

**-Reinicio automático**

Cuando se muestran todas las frases, el sistema vuelve al inicio automáticamente, permitiendo repetir el ciclo indefinidamente.

# ¿Cómo funciona internamente?

La aplicación utiliza una arquitectura reactiva basada en:

**-Estado (State):**
Guarda el índice actual, la lista de frases, el mensaje mostrado y el color del texto.

**-Lista de frases:**
Contiene tanto mensajes de invitación como frases motivacionales organizadas en un orden específico.

**-Evento (interactuar):**
Función en Python que se ejecuta al hacer clic y cambia a la siguiente frase.

**-Control del ciclo:**
El sistema avanza en la lista y, al llegar al final, vuelve al inicio automáticamente.

**-Interfaz (UI):**
Se actualiza en tiempo real cuando cambia el estado, sin necesidad de recargar la página.

Esto permite una experiencia interactiva continua, donde cada clic genera una nueva respuesta visual, haciendo que la página se sienta dinámica y viva.

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



