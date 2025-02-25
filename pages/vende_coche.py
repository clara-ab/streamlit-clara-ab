
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# Libraría para poder generar números aleatorios:
import random

# # # # #  FIN LIBRERÍAS # # # # #


# # # # #  INICIO FUNCIÓN VENDE COCHE # # # # #

# Título:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 🚗 Vende tu coche usado 🚗 </h1>", unsafe_allow_html = True);

# Subtítulo: 
st.markdown("<h3 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> \n\nInformación de tu Coche\n\n </h3>", unsafe_allow_html = True);

# Campos a Rellenar:
brand = st.text_input ("Marca de tu Coche");
year = st.number_input ("Año de Fabriación de tu Coche", min_value = 1900, max_value = 2025);
seats = st.number_input ("Número de Plazas de tu Coche", min_value = 1, max_value = 7);
km = st.number_input ("Número de KM recorridos", min_value = 0);

# Espacio para subir Foto:
st.markdown("<h3 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> \n\nNuestra IA valora el estado de tu Coche a través de una foto</h3>", unsafe_allow_html = True);
image = st.file_uploader("Foto de tu Coche", type = ["jpg", "jpeg", "png"]);

# Botón Calcular Precio:
if st.button("Calcular Precio de Venta"):
    if brand and year and seats and km and image: # Se comprueba que todos los campos están rellenados y con valores adecuados
        price = random.randint(10000, 80000);
        st.markdown(f"### El precio estimado de tu coche es: **{price}€**");

    else:
        st.warning("Por favor, completa todos los campos antes de generar el precio.");
    


# Botón para volver al inicio en la barra lateral
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("streamlit_main");

# # # # #  FIN FUNCIÓN VENDE COCHE # # # # #