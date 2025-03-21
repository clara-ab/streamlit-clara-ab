
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #

# # # # #  INICIO FUNCIÓN TASAR COCHE PARTICULAR (2) # # # # #

# Se aplica un color de fondo #f5dae0:
page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fffafe;
    }
    </style>
    """
st.markdown(page_bg_color, unsafe_allow_html = True);

# Función para validar si un texto contiene solo letras
def validar_letras(texto): return texto.isalpha();

# Función para validar el correo electrónico
def validar_email(email): return '@' in email and '.' in email;

# Título:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 👩🏽🚘 Tasar Coche Particular 🛻👨🏼 </h1>", unsafe_allow_html = True);

st.markdown("## DATOS BÁSICOS")
anio_fabricacion = st.number_input("Año de fabricación del coche:", min_value=1900, max_value=2025)
fabricante = st.text_input("Fabricante:")
if fabricante and not validar_letras(fabricante):
    st.error("El fabricante solo puede contener letras.")

modelo = st.text_input("Modelo:")
tipo_coche = st.selectbox("Tipo de Coche:", ["Sedan", "SUV", "Hatchback", "Convertible", "Coupe", "Wagon", "Truck", "Van"])
estado_coche = st.selectbox("Estado del Coche:", ["Nuevo", "Usado", "Para repuestos"])
numero_millas = st.number_input("Número de Millas:", min_value=0)
color_coche = st.text_input("Color del coche:")

# Añadir espacio con <br> (salto de línea) para un margen más grande
st.markdown("<br>", unsafe_allow_html=True);

if st.button("Siguiente  ➡️  Detalles Técnicos"): 
    switch_page("tasar_coche_particular_tecnicos_page");

# Botón para volver al inicio en la barra lateral
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("test");


# # # # #  FIN FUNCIÓN TASAR COCHE PARTICULAR (2) # # # # #