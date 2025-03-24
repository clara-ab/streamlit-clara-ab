
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para poder utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #

 # Se configura la página para aprovechar todo el espacio:
st.set_page_config(page_title="Sobre Nosotros - Clara's Car Corner", page_icon=":car:", layout="wide");

# Se aplica el color de fondo deseado:
page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fffafe;
    }
    </style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True);

# Título
st.markdown("<h1 style='text-align: center; font-family: \"Droid Sans Mono\", monospace;'>Sobre Nosotros</h1>", unsafe_allow_html=True);

# Espacio
st.markdown("<br>", unsafe_allow_html=True);

# Introducción sobre la empresa
st.markdown("""
    ## ¡Conoce al equipo de Clara's Car Corner! 🚗✨

    En **Clara's Car Corner**, no solo nos apasionan los coches, ¡nos apasiona ayudar a las personas!  
    Somos un equipo de **profesionales dedicados** a ofrecer un **servicio de venta de coches de segunda mano** sencillo, **rápido**, y **confiable**. Sabemos lo difícil que puede ser vender un coche, y estamos aquí para hacer que ese proceso sea **fácil**, **transparente** y **sin estrés**.

    ### ¿Quiénes somos?
    Somos un grupo de **expertos en la industria automotriz**, con años de experiencia en la tasación de vehículos, análisis de mercado y servicio al cliente. Nos enorgullece ofrecer a nuestros clientes un **valor justo** por su coche y un proceso sin complicaciones.  
    Pero no solo eso, nuestro equipo también está compuesto por **tecnólogos y matemáticos** que han creado un algoritmo avanzado para calcular de manera precisa el valor de tu coche. 🚗💨
""");

# Imagen del equipo
st.image("images/equipo.png", use_container_width=True);

# Espacio
st.markdown("<br>", unsafe_allow_html=True);

# Enfoque en el servicio
st.markdown("""
    ## Nuestro Enfoque: **Vender un coche nunca fue tan fácil** 🚙✨

    En Clara's Car Corner, sabemos que la venta de un coche puede ser un proceso largo y complicado, por eso lo simplificamos para ti.  
    Con nuestra plataforma, podrás vender tu coche en solo tres sencillos pasos:

    - **Regístralo rápidamente**: Rellena un sencillo formulario con la información básica de tu coche.
    - **Obtén una tasación precisa**: Usamos tecnología avanzada para calcular el valor justo de tu coche.
    - **Vende en minutos**: Una vez aceptes la tasación, nos encargamos del resto.

    Lo más importante para nosotros es **tu confianza**. Queremos que sientas que el proceso es justo y transparente en todo momento.
""")

# Espacio
st.markdown("<br>", unsafe_allow_html=True);

# Sección de Trabaja con Nosotros
st.markdown("""
    ## ÚNETE A NUESTRO EQUIPO: ¡Buscamos talentos! 🚀

    Si te apasiona el mundo del automóvil, el análisis de datos y ofrecer un servicio de calidad a los clientes, **Clara's Car Corner** es el lugar ideal para ti.  
    Estamos buscando personas con **espíritu innovador** y **compromiso** para formar parte de nuestro equipo. Ya sea que tengas experiencia en el sector automotriz o en tecnología, ¡queremos saber de ti!  
    
    ### ¿Cómo puedes unirte?
    - **Consultor de ventas**: Ayuda a nuestros clientes a encontrar el mejor precio para sus coches.
    - **Ingeniero de software**: Mejora nuestros algoritmos y optimiza la plataforma.
    - **Especialista en marketing digital**: Ayuda a crecer nuestra comunidad online.
    
    Si estás interesado, **envíanos tu CV** a nuestra dirección de correo electrónico:  
    📧 **trabaja@clarascarcorner.com**

    ¡Te estamos esperando! 🌟
""")

# Espacio
st.markdown("<br>", unsafe_allow_html=True)

# Sección de opiniones en tarjetitas deslizables
st.markdown("## Lo que dicen nuestros clientes 🗣️💬")

# Definir las opiniones de los clientes
opiniones = [
    {"nombre": "Ana, Madrid", "texto": "¡Fue una experiencia increíble! El proceso de tasación fue rápido y transparente. ¡Vender mi coche fue mucho más fácil de lo que pensaba!"},
    {"nombre": "Jorge, Barcelona", "texto": "El equipo de Clara's Car Corner me ayudó a obtener un precio justo por mi coche. Todo fue muy profesional y sin complicaciones."},
    {"nombre": "María, Valencia", "texto": "Recomiendo totalmente esta plataforma. Me guiaron en cada paso y me dieron el valor exacto de mi coche."},
    {"nombre": "Carlos, Sevilla", "texto": "La plataforma es fácil de usar, y el servicio es excelente. Me ayudaron a vender mi coche sin estrés. ¡Muy recomendados!"}
]

# Creación de carrusel de opiniones con botones de navegación
current_opinion = st.session_state.get("current_opinion", 0)

# Mostrar la opinión actual
opinion = opiniones[current_opinion]
st.markdown(f"### {opinion['nombre']}")
st.markdown(f"\"{opinion['texto']}\"")

# Botones de navegación para cambiar la opinión
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("Anterior"):
        current_opinion = (current_opinion - 1) % len(opiniones)
        st.session_state["current_opinion"] = current_opinion

with col3:
    if st.button("Siguiente"):
        current_opinion = (current_opinion + 1) % len(opiniones)
        st.session_state["current_opinion"] = current_opinion

# Espacio
st.markdown("<br>", unsafe_allow_html=True)

# # # # # INICIO SOBRE NOSOTROS FUNCTION # # # # #

# # # # # FIN SOBRE NOSOTROS FUNCTION # # # # #