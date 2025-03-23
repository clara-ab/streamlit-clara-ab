
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #


# # # # #  INICIO FUNCIÓN PARTICULAR # # # # #

# Se configura la página para poder aprovechar toda la página:
st.set_page_config(page_title = "👩🏽 Particular 👨🏼", page_icon = ":car:", layout = "wide");

# Se aplica un color de fondo deseado #ffe3e8:
page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #ffe3e8;
    }
    </style>
    """
st.markdown(page_bg_color, unsafe_allow_html = True);


# Título - 👩🏽 Particular 👨🏼:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 👩🏽 Particular 👨🏼 </h1>", unsafe_allow_html = True);

# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html=True);

# Se crean dos columnas para poner la imagen y el texto al lado:
col1, col2 = st.columns([1, 2])  # Se coloca una proporción de 1/2 para que el texto ocupe más que la imagen

# Columna 1 - Imagen:
with col1:
    st.image("images/particular_door_image.png", use_container_width = True);

# Columna 2 - Texto:
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
    """);

# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html=True);

# Botón - Inicio Proceso de Tasación:
if st.button("Iniciar proceso de tasación"): switch_page("tasar_coche_particular_intro_page");  # Si se pulsa pasa a la siguiente página


# Botón para volver al inicio en la barra lateral:
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("main_page");

# # # # #  FIN FUNCIÓN PARTICULAR # # # # #