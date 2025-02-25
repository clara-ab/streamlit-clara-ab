
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #


# # # # # INICIO MAIN FUNCTION # # # # #
def main ():

    # Título:
    st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 🚗 Compra y Vende tu Coche\n - Coches de Segunda Mano 🚗 </h1>", unsafe_allow_html=True);

    # Subtítulo: 
    st.markdown("<h3 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> \n\n¿Quieres comprar o vender?\n\n </h3>", unsafe_allow_html=True);

    # Botones de selección:
    col1, col2 = st.columns(2) # Se crean dos "columnas" para organizar los botones en disposición horizontal:
    with col1:
        #if st.button("Quiero un coche nuevo"): st.write("Has seleccionado: Quiero un coche nuevo.");
        if st.button("Quiero un coche nuevo"):  switch_page("compra_coche");
    with col2:
        if st.button("Quiero vender mi coche"): switch_page("vende_coche");
    
if __name__ == "__main__":
    main()


# # # # # FIN MAIN FUNCTION # # # # #
