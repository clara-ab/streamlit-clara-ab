# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #


# # # # # INICIO MAIN FUNCTION # # # # #
def main ():

    # Estilo de fondo
    page_bg_color = """
    <style>
    body {
        background-color: #fa2f5b; 
    }
    </style>
    """
    st.markdown(page_bg_color, unsafe_allow_html=True)


    # Título:
    st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 🚗 VENDE TU COCHE 🚗 </h1>", unsafe_allow_html=True);

    # Subtítulo: 
    st.markdown("<h3 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> \n\n¿Eres un particular o una empresa?\n\n </h3>", unsafe_allow_html=True);

    
    # Botones de selección:
    col1, col2 = st.columns(2) # Se crean dos "columnas" para organizar los botones en disposición horizontal:
    with col1:
        #if st.button("Quiero un coche nuevo"): st.write("Has seleccionado: Quiero un coche nuevo.");
        if st.button("Particular"):  switch_page("particular_page");
    with col2:
        if st.button("Empresa"): switch_page("empresa_page");
    
if __name__ == "__main__":
    main()


# # # # # FIN MAIN FUNCTION # # # # #