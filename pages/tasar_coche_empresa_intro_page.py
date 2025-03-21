
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #


# # # # #  INICIO FUNCIÓN TASAR COCHE EMPRESA (1) # # # # #

# Se aplica un color de fondo #f5dae0:
page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fffafe;
    }
    </style>
    """
st.markdown(page_bg_color, unsafe_allow_html = True);

# Título:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 🏢🚘 Tasación - Flota Empresa 🛻🏣 </h1>", unsafe_allow_html = True);

# Formulario de Datos de la Empresa
st.markdown("## Datos de la Empresa")

# Campo Nombre de la Empresa
nombre_empresa = st.text_input("Nombre de la Empresa:", max_chars=100)

# Campo CIF
cif_empresa = st.text_input("CIF de la Empresa:", max_chars=9)

# Campo Domicilio Fiscal
domicilio_fiscal = st.text_input("Domicilio Fiscal:", max_chars=200)

# Campo Teléfono de contacto
telefono_contacto = st.text_input("Teléfono de Contacto:", max_chars=15)

# Campo Correo electrónico
email_contacto = st.text_input("Correo Electrónico de Contacto:", max_chars=100)

# Campo Persona de contacto
persona_contacto = st.text_input("Persona de Contacto en la Empresa:", max_chars=100)


# Añadir espacio con <br> (salto de línea) para un margen más grande
st.markdown("<br>", unsafe_allow_html=True);


# Instrucciones adicionales antes de la descarga
st.write("""
    ## Instrucciones para completar el archivo CSV
    
    A continuación, puedes descargar el archivo **CSV modelo** que te ayudará a completar la información de los coches que deseas vender. Este archivo contiene todas las columnas necesarias para una correcta tasación.

    **Importante:** Asegúrate de que el archivo CSV esté correctamente formateado con los datos requeridos para que podamos realizar una tasación precisa.

    ---
""")

# Ruta del archivo de Excel que deseas ofrecer para descarga (ajústala según tu estructura de archivos)
archivo_modelo = "data/raw/test_excel.csv"

# Botón para descargar el archivo
with open(archivo_modelo, "rb") as f:
    st.download_button(
        label = "📥 Descargar Excel Modelo",
        data = f,
        file_name = "modelo_coche.xlsx",
        mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


# Añadir espacio con <br> (salto de línea) para un margen más grande
st.markdown("<br>", unsafe_allow_html=True);


st.write("""
    ---
    
    ## Subir tu archivo completado
    
    Una vez que hayas completado el archivo CSV con todos los detalles de los coches que deseas vender, puedes **subirlo** en el espacio que se encuentra a continuación.

    **Recuerda:** Verifica que el archivo esté correctamente formateado y contenga toda la información necesaria para cada vehículo. Nosotros procesaremos el archivo y te devolveremos las tasaciones correspondientes para cada coche.

    ¡**Sube tu archivo** para continuar con la tasación!
""")

# Subida de archivo CSV
archivo_coche = st.file_uploader("Sube el archivo CSV con los coches a vender", type = "csv");

# # # # #  FIN FUNCIÓN TASAR COCHE EMPRESA (1) # # # # #