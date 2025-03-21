
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #

# # # # #  INICIO FUNCIÓN PARTICULAR # # # # #

# Configuración de la página
st.set_page_config(page_title = "👩🏽 Particular 👨🏼", page_icon=":car:", layout="wide")

# Se aplica un color de fondo #f5dae0:
page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #ffe3e8;
    }
    </style>
    """
st.markdown(page_bg_color, unsafe_allow_html = True);

# Título:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 👩🏽 Particular 👨🏼 </h1>", unsafe_allow_html = True);

# Añadir espacio con <br> (salto de línea) para un margen más grande
st.markdown("<br>", unsafe_allow_html=True);

# Crear columnas para poner la imagen y el texto al lado
col1, col2 = st.columns([1, 2])  # Proporción de espacio, la imagen en la columna más pequeña (col1) y el texto en la más grande (col2)

# Columna 1: Imagen (al margen izquierdo)
with col1:
    st.image("images/particular_door_image.png", use_container_width = True)

# Columna 2: Texto
with col2:
    st.write("""
        ### 🚘 ¿Eres un particular y quieres vender tu coche?  

        ¡Estás en el lugar adecuado! En **Vende Tu Coche**, hemos diseñado un proceso simple y sin complicaciones para ayudarte a vender tu vehículo de manera rápida y eficiente.  
        Nuestro objetivo es que obtengas una valoración justa y transparente sin perder tiempo.  

        ### 🛠 ¿Cómo funciona?  
        1. **Introduce los datos de tu coche**: modelo, año, kilometraje, estado y otros detalles.  
        2. **Nuestro sistema calculará un precio justo** basado en múltiples factores del mercado actual.  
        3. **Recibe tu tasación al instante** y decide si deseas continuar con la venta.  

        ### 🔹 ¿Por qué elegirnos?  
        ✅ **Proceso rápido y transparente**: sin papeleo complicado ni largas esperas.  
        ✅ **Sin comisiones ocultas**: la tasación es completamente gratuita y sin compromisos.  
        ✅ **Asesoramiento personalizado**: nuestro equipo está aquí para responder cualquier duda y ayudarte en el proceso.  

        No importa el modelo ni el estado de tu coche, en nuestra plataforma encontrarás un proceso **seguro, confiable y sin complicaciones**.  

        🚀 **¡Empieza ahora y obtén tu tasación en minutos!**  
    """)

    # Añadir espacio con <br> (salto de línea) para un margen más grande
st.markdown("<br>", unsafe_allow_html=True);

# Añadir un botón para iniciar el proceso de tasación
if st.button("Iniciar proceso de tasación"):
    # Este botón redirige a la página donde se iniciará el proceso de tasación
    switch_page("tasar_coche_particular_intro_page")  # Cambia a la página de tasación


# Botón para volver al inicio en la barra lateral
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("test");

# # # # #  FIN FUNCIÓN PARTICULAR # # # # #