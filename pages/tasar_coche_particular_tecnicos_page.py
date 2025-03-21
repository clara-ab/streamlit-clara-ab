
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

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

# Función para validar si un texto contiene solo letras
def validar_letras(texto): return texto.isalpha();

# Función para validar el correo electrónico
def validar_email(email): return '@' in email and '.' in email;

# Sección de Detalles Técnicos
st.markdown("## DETALLES TÉCNICOS");

tipo_combustible = st.selectbox("Tipo de Combustible:", ["Gas", "Diesel", "Electric", "Other"]);

numero_cilindrada = st.number_input("Número de Cilindrada:", min_value=1);

tipo_traccion = st.selectbox("Tipo de Tracción:", ["RWD", "FWD", "4WD"]);

tipo_transmision = st.selectbox("Tipo de Transmisión:", ["Manual", "Automático", "Other"]);

# Añadir espacio con <br> (salto de línea) para un margen más grande
st.markdown("<br>", unsafe_allow_html=True);

# Explicación sobre la imagen
st.write("""
Para mejorar la precisión de la tasación y facilitar la revisión por parte de nuestros técnicos, 
puedes subir una imagen de tu coche. Esto nos ayudará a evaluar mejor su estado y tenerlo 
como referencia en nuestra base de datos.
""")

# Subir imagen
imagen_coche = st.file_uploader("Sube una imagen de tu coche (opcional)", type = ["jpg", "jpeg", "png"])

if imagen_coche:
    st.image(imagen_coche, caption = "Imagen subida", use_container_width = True)


# Botón para volver al inicio en la barra lateral
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("test");

# # # # #  FIN FUNCIÓN TASAR COCHE PARTICULAR (3) # # # # #