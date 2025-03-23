
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #


# # # # #  INICIO FUNCIÓN TASAR COCHE PARTICULAR (3) # # # # #

# Se configura la página para poder aprovechar toda la página:
st.set_page_config(page_title = "👩🏽 Tasación - Particular 👨🏼", page_icon = ":car:", layout = "wide");

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
tipo_combustible = st.selectbox("Tipo de Combustible:", ['gas', 'diesel', 'hybrid', 'electric', 'other']);
st.session_state.tipo_combustible = tipo_combustible;  # Se guarda el tipo de combustible para poder invocarlo donde sea

# Campo - Número de Cilindrada:
numero_cilindrada = st.selectbox("Número de Cilindrada:", [0, 4, 6, 8, 10]);
st.session_state.numero_cilindrada = numero_cilindrada; # Se guarda el número de cilindrada para poder invocarlo donde sea

# Campo - Tracción:
tipo_traccion = st.selectbox("Tipo de Tracción:", ['4wd', 'rwd', 'fwd']);
st.session_state.tipo_traccion = tipo_traccion; # Se guarda el tipo de tracción para poder invocarlo donde sea

# Campo - Transmisión:
tipo_transmision = st.selectbox("Tipo de Transmisión:", ['automatic', 'other', 'manual']);
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


# Botón para realizar la predicción
if st.button("💸 Tasa mi coche 🚘"): switch_page("tasador_particular")


# Botón para volver al inicio en la barra lateral:
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("main_page");

# # # # #  FIN FUNCIÓN TASAR COCHE PARTICULAR (3) # # # # #