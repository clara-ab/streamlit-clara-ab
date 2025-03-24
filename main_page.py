# # # # # INICIO LIBRERÍAS # # # # #

# Librería para poder utilizar Streamlit:
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #


# # # # # INICIO MAIN FUNCTION # # # # #
def main():
    # Se configura la página para poder aprovechar toda la página:
    st.set_page_config(page_title = "🚗 CLARA'S CAR CORNER 🚗", page_icon = ":car:", layout = "wide");
    
    # Se aplica un color de fondo deseado #fffafe:
    page_bg_color = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #fffafe;
        }
        </style>
        """
    st.markdown(page_bg_color, unsafe_allow_html = True);


    # Se añade un espacio:
    st.markdown("<br>", unsafe_allow_html = True);

    # Título - 🚗 CLARA'S CAR CORNER 🚗 :
    st.markdown("<h1 style = 'text-align: center'; font-family: 'Droid Sans Mono', monospace;'> 🚗 CLARA'S CAR CORNER 🚗 </h1>", unsafe_allow_html=True);
    
    # Se añade un espacio:
    st.markdown("<br>", unsafe_allow_html = True);

    # Imagen:
    st.image("images/portada_coches.png", use_container_width = True);

    # Se añade un espacio:
    st.markdown("<br>", unsafe_allow_html = True);

    # Texto introductorio para la página de la empresa:
    st.markdown("""
        # ¡Bienvenido a **Clara's Car Corner**! 🚗✨

        **¿Estás buscando vender tu coche usado?**  
        ¡Estás en el lugar adecuado! En **Clara's Car Corner**, nos especializamos en ofrecer un proceso de venta de coches de segunda mano **transparente**, **rápido** y **sin complicaciones**. 💨

        ## ¿Por qué elegirnos? 🤔

        ### 1. **Tasación justa 💸**
        Utilizamos un algoritmo avanzado para ofrecerte una **estimación precisa** del valor de tu coche. Nuestro objetivo es asegurarnos de que obtengas un precio justo basado en el **modelo**, **año**, **kilometraje** y el **estado del vehículo**.

        ### 2. **Proceso sencillo 📝**
        Olvídate de trámites complicados. Con nuestra plataforma, solo tendrás que rellenar unos simples datos, y nosotros nos encargaremos del resto. ¡Así de fácil! ✅

        ### 3. **Asesoramiento personalizado 💬**
        Si tienes alguna duda, **nuestro equipo de expertos está disponible** para ayudarte en todo momento. Te ofreceremos la mejor orientación para que tengas la experiencia más cómoda posible. 🤝

        ---

        Si **quieres vender tu coche 🚙**, estamos aquí para ayudarte a hacerlo de la manera más **fácil** y **segura** posible.  
        ¡Descubre todo lo que **Clara's Car Corner** tiene para ofrecerte! 🌟
    """);

    # Subtítulo: 
    st.markdown("<h3 style = 'text-align: center'; font-family: 'Droid Sans Mono', monospace;'>¿Eres un particular o una empresa?</h3>", unsafe_allow_html=True);
    
    # Se añade un espacio:
    st.markdown("<br>", unsafe_allow_html = True);

    # Botones - Particular vs. Empresa:
    col1, col2, col3 = st.columns([1, 1, 1]);

    with col2:
        col_a, col_b = st.columns(2);
    
        with col_a:
            if st.button("Particular"): 
                switch_page("particular_page");
        
        with col_b:
            if st.button("Empresa"): 
                switch_page("empresa_page");

if __name__ == "__main__":
    main()

# # # # # FIN MAIN FUNCTION # # # # #
