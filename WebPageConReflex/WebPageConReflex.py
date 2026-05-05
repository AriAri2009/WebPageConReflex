

import reflex as rx

# --- 1. EL ESTADO (Lógica detrás del botón) ---
class State(rx.State):
    
    mensaje: str = "¡Haz clic en el botón para ver la magia!"

    color_texto: str = "var(--gray-11)"

    @rx.event
    def interactuar(self):
        
        if self.mensaje == "¡Haz clic en el botón para ver la magia!":
            self.mensaje = "🎉 ¡Felicidades! ¡Lograste interactuar con el botón de mi página web!"
            self.color_texto = "var(--accent-10)"
        else:
            
            self.mensaje = "¡Haz clic en el botón para ver la magia!"
            self.color_texto = "var(--gray-11)"


# --- 2. LA INTERFAZ DE USUARIO (Diseño Visual) ---
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
          
            rx.heading(
                "Primera Página Web con Reflex de Arianna Cedeño", 
                size="8", 
                weight="bold",
                font_style="italic",
                color_scheme="indigo",
                align="center"
            ),
            
            
            rx.text(
                "¡Bienvenido/a a este simple y pequeño proyecto!",
                font_size="1.4em",
                color_scheme="gray",
                weight="medium"
            ),
            
            
            rx.box(
                rx.text(
                    State.mensaje, 
                    font_size="1.2em", 
                    font_style="italic",
                    color=State.color_texto
                ),
                padding="4",
                border_radius="md",
                background_color="var(--gray-2)",
                border="1px solid var(--gray-4)",
                width="100%"
            ),
            
     
            rx.button(
                "Interactuar",
                on_click=State.interactuar,  # Al hacer clic, ejecuta la función del Estado
                size="3",
                color_scheme="indigo",
                cursor="pointer",
                variant="classic"
            ),
            
            spacing="5",         # Espaciado entre elementos
            align="center",      # Centrar horizontalmente todo dentro de la columna
            max_width="600px",   # Limita el ancho del contenido para que se vea ordenado
            width="100%"
        ),
        width="100%",
        height="100vh",          # Ocupa todo el alto de la pantalla para centrar la página verticalmente
        background_color="var(--gray-1)" # Un fondo sutilmente gris claro/oscuro según el tema
    )


app = rx.App()
app.add_page(index)
