
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #

# # # # #  INICIO FUNCIÓN TASAR COCHE PARTICULAR (1) # # # # #

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

# Lista de estados de EE.UU. con las siglas
estados_eeuu = [
    'Alabama (AL)', 'Alaska (AK)', 'Arizona (AZ)', 'Arkansas (AR)', 'California (CA)', 'Colorado (CO)', 'Connecticut (CT)', 
    'Delaware (DE)', 'Florida (FL)', 'Georgia (GA)', 'Hawaii (HI)', 'Idaho (ID)', 'Illinois (IL)', 'Indiana (IN)', 'Iowa (IA)', 
    'Kansas (KS)', 'Kentucky (KY)', 'Louisiana (LA)', 'Maine (ME)', 'Maryland (MD)', 'Massachusetts (MA)', 'Michigan (MI)', 
    'Minnesota (MN)', 'Mississippi (MS)', 'Missouri (MO)', 'Montana (MT)', 'Nebraska (NE)', 'Nevada (NV)', 'New Hampshire (NH)', 
    'New Jersey (NJ)', 'New Mexico (NM)', 'New York (NY)', 'North Carolina (NC)', 'North Dakota (ND)', 'Ohio (OH)', 
    'Oklahoma (OK)', 'Oregon (OR)', 'Pennsylvania (PA)', 'Rhode Island (RI)', 'South Carolina (SC)', 'South Dakota (SD)', 
    'Tennessee (TN)', 'Texas (TX)', 'Utah (UT)', 'Vermont (VT)', 'Virginia (VA)', 'Washington (WA)', 'West Virginia (WV)', 
    'Wisconsin (WI)', 'Wyoming (WY)', 'Washington D.C. (DC)'
]

# Título:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 👩🏽🚘 Tasar Coche Particular 🛻👨🏼 </h1>", unsafe_allow_html = True);


# Sección de Datos de Contacto
st.markdown("## DATOS DE CONTACTO")
nombre = st.text_input("Nombre:")
if nombre and not validar_letras(nombre):
    st.error("El nombre solo puede contener letras.")

apellidos = st.text_input("1er Apellido:")
if apellidos and not validar_letras(apellidos):
    st.error("Los apellidos solo pueden contener letras.")

email = st.text_input("Correo electrónico:")
if email and not validar_email(email):
    st.error("Por favor ingresa un correo electrónico válido.")

telefono = st.text_input("Número de Teléfono:")
if telefono and not telefono.isdigit():
    st.error("El número de teléfono solo puede contener números.")
    
estado_seleccionado = st.selectbox("Selecciona el estado de EE.UU.:", estados_eeuu)

# Añadir espacio con <br> (salto de línea) para un margen más grande
st.markdown("<br>", unsafe_allow_html=True);

if st.button("Siguiente  ➡️  Datos Básicos"): 
    switch_page("tasar_coche_particular_basic_page");

# Botón para volver al inicio en la barra lateral
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("test");

# # # # #  FIN FUNCIÓN TASAR COCHE PARTICULAR (1) # # # # #