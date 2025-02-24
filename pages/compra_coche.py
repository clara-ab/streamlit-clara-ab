
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page


# # # # #  FIN LIBRERÍAS # # # # #

# # # # #  INICIO FUNCIÓN COMPRA COCHE # # # # #

# Título:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 🚗 Compra tu coche nuevo 🚗 </h1>", unsafe_allow_html=True);

# Subtítulo: 
st.markdown("<h3 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> \n\nSelecciona tu Futuro Coche\n\n </h3>", unsafe_allow_html=True);

# Imágenes a seleccionar:
images = [
    {"img": "images/audi.jpg", "precio": "15.000€", "marca": "Fiat", "año": "2020", "Plazas": "4"},
    {"img": "images/fiat.jpg", "precio": "35.000€", "marca": "Audi", "año": "2019", "Plazas": "5"},
    {"img": "images/citroen.jpg", "precio": "10.000€", "marca": "Citroen", "año": "2018", "Plazas": "7"},
    {"img": "images/volvo.jpg", "precio": "30.000€", "marca": "Volvo", "año": "2021", "Plazas": "7"},
    {"img": "images/polestar.jpg", "precio": "25.000€", "marca": "Polestar", "año": "2020", "Plazas": "5"},
    {"img": "images/mercedes.jpg", "precio": "55.000€", "marca": "Mercedes", "año": "2017", "Plazas": "5"}
];

col1, col2, col3 = st.columns(3); # Fila 1 con 3 columnas
with col1:
    st.image(images[0]["img"], caption = "Fiat");
with col2:
    st.image(images[1]["img"], caption = "Audi");
with col3:
    st.image(images[2]["img"], caption = "Citroen");

col4, col5, col6 = st.columns(3)

# Mostrar las imágenes en la segunda fila
with col4:
    st.image(images[3]["img"], caption="Volvo");
with col5:
    st.image(images[4]["img"], caption="Polestar");
with col6:
    st.image(images[5]["img"], caption="Mercedes");

# # # # #  FIN FUNCIÓN COMPRA COCHE # # # # #