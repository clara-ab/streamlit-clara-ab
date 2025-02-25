
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

# # # # #  FIN LIBRERÍAS # # # # #


# # # # #  INICIO FUNCIÓN COMPRA COCHE # # # # #

# Título:
st.markdown("<h1 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> 🚗 Compra tu coche nuevo 🚗 </h1>", unsafe_allow_html = True);

# Subtítulo: 
st.markdown("<h3 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> \n\nSelecciona tu Futuro Coche\n\n </h3>", unsafe_allow_html = True);

# Imágenes a seleccionar:
images = [
    {"img": "images/audi.jpg", "price": "35.000€", "brand": "Audi", "year": "2019", "seats": "5"},
    {"img": "images/fiat.jpg", "price": "15.000€", "brand": "Fiat", "year": "2021", "seats": "4"},
    {"img": "images/citroen.jpg", "price": "10.000€", "brand": "Citroen", "year": "2018", "seats": "7"},
    {"img": "images/volvo.jpg", "price": "30.000€", "brand": "Volvo", "year": "2021", "seats": "7"},
    {"img": "images/polestar.jpg", "price": "25.000€", "brand": "Polestar", "year": "2020", "seats": "5"},
    {"img": "images/mercedes.jpg", "price": "55.000€", "brand": "Mercedes", "year": "2017", "seats": "5"}
];

col1, col2, col3 = st.columns(3); # 1 Fila con 3 columnas
with col1:
    st.image(images[0]["img"], caption = "Audi");
with col2:
    st.image(images[1]["img"], caption = "Fiat");
with col3:
    st.image(images[2]["img"], caption = "Citroen");

col4, col5, col6 = st.columns(3); # 1 Fila con 3 columnas
with col4:
    st.image(images[3]["img"], caption = "Volvo");
with col5:
    st.image(images[4]["img"], caption = "Polestar");
with col6:
    st.image(images[5]["img"], caption = "Mercedes");

# Subtítulo: 
st.markdown("<h5 style = 'text-align: center'; font-family: \'Droid Sans Mono\', monospace;'> \n\n\nSelecciona el coche del que quieres saber más información\n\n </h5>", unsafe_allow_html = True);

# Botones de Selección:
if "selected_car" not in st.session_state: st.session_state.selected_car = None; # Se inicializa el estado de la selección para que se pueda guardar correctamente

col1, col2, col3, col4, col5, col6 = st.columns(6); # 1 Fila con 6 columnas
with col1:
    if st.button("Audi"): st.session_state.selected_car = "Audi";
with col2:
    if st.button("Fiat"): st.session_state.selected_car = "Fiat";
with col3:
    if st.button("Citroen"): st.session_state.selected_car = "Citroen";
with col4:
    if st.button("Volvo"): st.session_state.selected_car = "Volvo";
with col5:
    if st.button("Polestar"): st.session_state.selected_car = "Polestar";
with col6:
    if st.button("Mercedes"): st.session_state.selected_car = "Mercedes";

# Mensaje a mostrar dependiendo del botón seleccionado
for car in images: 
    if st.session_state.selected_car == car ['brand']:
        st.markdown(f"### 🚘 {car['brand']}");
        st.markdown(f"**Precio:** {car['price']}");
        st.markdown(f"**Año:** {car['year']}");
        st.markdown(f"**Plazas:** {car['seats']}");

     # Botón de Compra:
        if st.button("COMPRA"): st.markdown(f"### ¡¡¡ Se ha añadido un 🚘 {car['brand']} a la cesta!!!")
 

# Botón para volver al inicio en la barra lateral
if st.sidebar.button("🏠 Volver al Inicio"): switch_page("streamlit_main");

# # # # #  FIN FUNCIÓN COMPRA COCHE # # # # #