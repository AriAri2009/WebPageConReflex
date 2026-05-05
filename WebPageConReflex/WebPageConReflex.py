import reflex as rx

# --- 1. EL ESTADO (Lógica para rotar las 4 frases) ---
class State(rx.State):
    # Lista con las 4 frases diferentes que irán rotando
    frases: list[str] = [
        "¡Haz clic en el botón para ver la magia!",
        "¡Eres bonito/a, inteligente y capaz, nunca lo dudes!",
        "¡Haz clic en el botón para ver la magia!",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "¡Haz clic en el botón para ver la magia!",
        "¡No te dejes vencer! ¡Ahora es que tu camino esta iniciando!",
        "¡Haz clic en el botón para ver la magia!",
        "¡El único límite para tu impacto es tu propia imaginación!"
    ]
    
    # Lista con los colores correspondientes para cada frase (con buen contraste para el fondo)
    colores: list[str] = [
        "var(--gold-12)",     
        "var(--accent-11)",
        "var(--gold-12)",    
        "var(--orange-11)", 
        "var(--gold-12)",   
        "var(--indigo-11)" ,
        "var(--gold-12)",
        "var(--pink-12)"   
    ]
    
    # Controlamos en qué posición de la lista estamos actualmente
    indice_actual: int = 0

    # Variables dinámicas que la interfaz va a leer
    @rx.var
    def mensaje(self) -> str:
        return self.frases[self.indice_actual]

    @rx.var
    def color_texto(self) -> str:
        return self.colores[self.indice_actual]

    @rx.event
    def interactuar(self):
        # Avanzamos al siguiente índice cíclicamente
        self.indice_actual = (self.indice_actual + 1) % len(self.frases)


# --- 2. LA INTERFAZ DE USUARIO (Diseño Visual) ---
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
          
            rx.heading(
                "Frases motivacionales para mejorar tu día", 
                size="8", 
                weight="bold",
                font_style="italic",
                color_scheme="teal",
                align="center"
            ),
            
            rx.text(
                "¡Bienvenido/a a este simple y pequeño proyecto!",
                font_size="1.4em",
                color_scheme="ruby",
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
                background_color="rgba(255, 255, 255, 0.85)",  # Fondo blanco semitransparente para que el texto se lea perfecto sobre cualquier imagen
                border="1px solid var(--gray-4)",
                width="100%"
            ),
            
            rx.button(
                "Interactuar",
                on_click=State.interactuar, 
                size="3",
                color_scheme="pink",
                cursor="pointer",
                variant="classic"
            ),
            
            spacing="5",         
            align="center",      
            max_width="600px",  
            width="100%"
        ),
        width="100%",
        height="100vh",       
        
   
        background_image="url('/flores1.jpg')",  
        background_size="cover",                 
        background_position="center",             
        background_repeat="no-repeat"             
    )


app = rx.App()
app.add_page(index)