
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

import pickle

import pandas as pd

import sklearn

# # # # #  FIN LIBRERÍAS # # # # #


# # # # #  INICIO FUNCIÓN TASAR COCHE PARTICULAR (3) # # # # #

# Se aplica un color de fondo #f5dae0:
page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fffafe;
    }
    </style>
    """
st.markdown(page_bg_color, unsafe_allow_html = True);


# Función para validar si un texto contiene solo letras:
def validar_letras(texto): return texto.isalpha();

# Función para validar un correo electrónico:
def validar_email(email): return '@' in email and '.' in email;


# Título - 👩🏽🚘 Tasación - Coche Particular 🚗👨🏼 :
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 👩🏽🚘 Tasación - Coche Particular 🚗👨🏼 </h1>", unsafe_allow_html = True);

# Título - Detalles Técnicos:
st.markdown("## DETALLES TÉCNICOS");

# Campo - Tipo de Combustible:
tipo_combustible = st.selectbox("Tipo de Combustible:", ["Gas", "Diesel", "Electric", "Other"]);
st.session_state.tipo_combustible = tipo_combustible;  # Se guarda el tipo de combustible para poder invocarlo donde sea

# Campo - Número de Cilindrada:
numero_cilindrada = st.number_input("Número de Cilindrada:", min_value=1);
st.session_state.numero_cilindrada = numero_cilindrada; # Se guarda el número de cilindrada para poder invocarlo donde sea

# Campo - Tracción:
tipo_traccion = st.selectbox("Tipo de Tracción:", ["RWD", "FWD", "4WD"]);
st.session_state.tipo_traccion = tipo_traccion; # Se guarda el tipo de tracción para poder invocarlo donde sea

# Campo - Transmisión:
tipo_transmision = st.selectbox("Tipo de Transmisión:", ["Manual", "Automático", "Other"]);
st.session_state.tipo_transmision = tipo_transmision; # Se guarda el tipo de transmisión para poder invocarlo donde sea

# Se añade un espacio:
st.markdown("<br>", unsafe_allow_html=True);

# Texto introductorio a la subida de la posbilidad de subida imagen:
st.write("""
Para mejorar la precisión de la tasación y facilitar la revisión por parte de nuestros técnicos, 
puedes subir una imagen de tu coche. Esto nos ayudará a evaluar mejor su estado y tenerlo 
como referencia en nuestra base de datos.
""");

# Subida imagen:
imagen_coche = st.file_uploader("Sube una imagen de tu coche (opcional)", type = ["jpg", "jpeg", "png"]);

if imagen_coche: st.image(imagen_coche, caption = "Imagen subida", use_container_width = True); # Si se ha subido una imagen, se muestra:

# Cargar el modelo previamente guardado
with open("models/random_forest_grid_model.pkl", "rb") as file:
    modelo = pickle.load(file)

# Crear un DataFrame con los datos almacenados en session_state
data = {
    "region":"alabama",
    "year": [st.session_state.get("year_fabricacion", None)],
    "manufacturer": [st.session_state.get("fabricante", None)],
    "model": [st.session_state.get("modelo", None)],
    "condition": [st.session_state.get("estado_coche", None)],
    "cylinders": [st.session_state.get("numero_cilindrada", None)],
    "fuel": [st.session_state.get("tipo_combustible", None)],
    "odometer": [st.session_state.get("numero_millas", None)],
    "transmission": [st.session_state.get("tipo_transmision", None)],
    "drive": [st.session_state.get("tipo_traccion", None)],
    "type": [st.session_state.get("tipo_coche", None)],
    "paint_color": [st.session_state.get("color_coche", None)],
    "state": [st.session_state.get("estado", None)],
}

df_input = pd.DataFrame(data)

# Botón para realizar la predicción
if st.button("Realizar Predicción"):
    # Mostrar el DataFrame con los valores ingresados
    st.write("Datos ingresados para la predicción:", df_input)

    # Realizar la predicción
    prediccion = modelo.predict(df_input)

    # Mostrar el resultado
    st.success(f"El valor estimado del coche es: ${prediccion[0]:,.2f}")
    

# Botón para volver al inicio en la barra lateral:
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("test");

# # # # #  FIN FUNCIÓN TASAR COCHE PARTICULAR (3) # # # # #