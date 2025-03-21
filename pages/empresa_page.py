
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #

# # # # #  INICIO FUNCIÓN EMPRESA # # # # #

# Configuración de la página
st.set_page_config(page_title = "🏢 Empresa 🏣", page_icon=":car:", layout="wide")


# Se aplica un color de fondo #f5dae0:
page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #f5dae0;
    }
    </style>
    """
st.markdown(page_bg_color, unsafe_allow_html = True);

# Título:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 🏢 Empresa 🏣 </h1>", unsafe_allow_html = True);

# Añadir espacio con <br> (salto de línea) para un margen más grande
st.markdown("<br>", unsafe_allow_html=True);

# Crear columnas para poner la imagen y el texto al lado
col1, col2 = st.columns([1, 3])  # Proporción de espacio, la imagen en la columna más pequeña (col1) y el texto en la más grande (col2)

# Columna 1: Imagen (al margen izquierdo)
with col1:
    st.image("images/empresa_image.png", use_container_width = True)

# Columna 2: Texto
with col2:
    st.write("""
        ### 🚛 Empresas: Vende tu Flota de Vehículos de Manera Eficiente  

        Si representas a una empresa y buscas vender varios vehículos a la vez, hemos diseñado una solución ágil y efectiva para ti. 
        Sabemos que el proceso de tasación puede ser tedioso cuando se trata de gestionar una flota, por lo que hemos simplificado 
        cada paso para que puedas obtener una valoración rápida y precisa.  

        En **Vende Tu Coche**, ofrecemos una herramienta que te permite subir un archivo **.CSV** con los datos de todos los vehículos 
        que deseas vender. Nuestro sistema analizará la información y tasará cada coche de manera individual utilizando nuestro algoritmo avanzado, 
        considerando factores como el modelo, el año de fabricación, el kilometraje y el estado general del vehículo.  

        ### 🚀 ¿Cómo funciona?  
        1. **Prepara tu archivo CSV** con los datos básicos de los vehículos que deseas vender.  
        2. **Súbelo a nuestra plataforma** con un solo clic.  
        3. **Recibe la tasación**: nuestro sistema analizará cada coche y te devolverá el mismo archivo CSV con la valoración correspondiente.  

        ### 🔹 ¿Por qué elegirnos?  
        ✅ **Ahorro de tiempo**: olvídate de introducir los datos manualmente coche por coche. Con un solo archivo, puedes tasar toda tu flota.  
        ✅ **Tasaciones precisas y transparentes**: nuestra tecnología analiza cada vehículo de manera objetiva, asegurando precios justos y actualizados.  
        ✅ **Proceso automatizado y seguro**: manejamos tus datos con total confidencialidad y sin complicaciones.  

        Si tu empresa busca vender coches de manera rápida y eficiente, **nuestra plataforma es la mejor opción**. 
        Con un proceso 100% digital, sencillo y sin papeleo innecesario, te ayudamos a gestionar la venta de tu flota sin complicaciones.  

        💼 **Optimiza el proceso de venta de tus vehículos con nuestra herramienta de tasación automatizada. ¡Súbelo ahora y obtén la mejor oferta!**  
    """)

# Añadir espacio con <br> (salto de línea) para un margen más grande
st.markdown("<br>", unsafe_allow_html=True);


# Botón para volver al inicio en la barra lateral
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("test");

# # # # #  FIN FUNCIÓN EMPRESA # # # # #