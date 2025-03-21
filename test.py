# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #


# # # # # INICIO MAIN FUNCTION # # # # #
def main ():
    # Configuración de la página
    st.set_page_config(page_title = "🚗 VENDE TU COCHE 🚗", page_icon=":car:", layout="wide")

    # Se aplica un color de fondo #ffe3e8:
    page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #ffe3e8;
    }
    </style>
    """
    st.markdown(page_bg_color, unsafe_allow_html = True);


    # Título:
    st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 🚗 VENDE TU COCHE 🚗 </h1>", unsafe_allow_html = True);
    
    # Añadir espacio con <br> (salto de línea) para un margen más grande
    st.markdown("<br>", unsafe_allow_html=True);

    # Imagen:
    st.image("images/portada_coches.png", use_container_width = True);

    # Añadir espacio con <br> (salto de línea) para un margen más grande
    st.markdown("<br>", unsafe_allow_html=True);

    # Subtítulo: 
    st.markdown("<h3 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'>¿Eres un particular o una empresa?</h3>", unsafe_allow_html = True);
    
    # Añadir espacio con <br> (salto de línea) para un margen más grande
    st.markdown("<br>", unsafe_allow_html=True);

    # Botones:
    # Se crean tres columnas para solo rellenar la del medio:
    col1, col2, col3 = st.columns([1, 1, 1]);

    with col2:

        # Se generan dos columnas en la columna del medio para los dos botones:
        col_a, col_b = st.columns(2);
    
    # Botón "Particular":
    with col_a:
        if st.button("Particular"): switch_page("particular_page"); # Si lo pulsan, se cambia de página:
    
    # Botón "Empresa":
    with col_b:
        if st.button("Empresa"): switch_page("empresa_page"); # Si lo pulsan, se cambia de página:
    
    # Botones de selección:
    #col1, col2 = st.columns(2) # Se crean dos "columnas" para organizar los botones en disposición horizontal:
    #with col1:
        #if st.button("Quiero un coche nuevo"): st.write("Has seleccionado: Quiero un coche nuevo.");
        #if st.button("Particular"):  switch_page("particular_page");
    #with col2:
        #if st.button("Empresa"): switch_page("empresa_page");
    
if __name__ == "__main__":
    main()


# # # # # FIN MAIN FUNCTION # # # # #