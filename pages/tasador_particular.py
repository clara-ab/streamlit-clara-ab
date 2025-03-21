
# # # # # INICIO LIBRERÍAS # # # # #

# Librería para pdoer utilizar Streamlit
import streamlit as st

# Librería para poder cambiar de páginas de visualización:
from streamlit_extras.switch_page_button import switch_page

import pickle

import pandas as pd

import sklearn

import numpy as np

from huggingface_hub import hf_hub_download

# # # # #  FIN LIBRERÍAS # # # # #

# Función para cargar el modelo desde Hugging Face
def cargar_modelo():
    # Descargar el modelo desde Hugging Face
    modelo_path = hf_hub_download(repo_id="clara-ab/random_forest_grid_model", filename="random_forest_grid_model.pkl")
    
    # Cargar el modelo descargado
    with open(modelo_path, "rb") as file:
        modelo = pickle.load(file)
    
    return modelo

# Función para cargar los encoders desde Hugging Face
def cargar_encoders():
    # Descargar el archivo de encoders desde Hugging Face
    encoders_path = hf_hub_download(repo_id="clara-ab/random_forest_grid_model", filename="encoders.pkl")
    
    # Cargar los encoders desde la ruta descargada
    with open(encoders_path, "rb") as file:
        encoders = pickle.load(file)
    
    return encoders


# # # # #  INICIO TASADOR PARTICULAR  # # # # #

# Se aplica un color de fondo #f5dae0:
page_bg_color = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fffafe;
    }
    </style>
    """
st.markdown(page_bg_color, unsafe_allow_html = True);


# Cargar el modelo previamente guardado
modelo = cargar_modelo();

# Crear un DataFrame con los datos almacenados en session_state
data = {
    "region":[st.session_state.get("region_estado", None)],
    "year": [st.session_state.get("year_fabricacion", None)],
    "manufacturer": [st.session_state.get("fabricante", None)],
    "model": [st.session_state.get("modelo", None)],
    "condition": [st.session_state.get("estado_coche", None)],
    "cylinders": [st.session_state.get("numero_cilindrada", None)],
    "fuel": [st.session_state.get("tipo_combustible", None)],
    "odometer": [st.session_state.get("numero_millas", None)],
    "transmission": [st.session_state.get("tipo_transmision", None)],
    "drive": [st.session_state.get("tipo_traccion", None)],
    "type": [st.session_state.get("tipo_coche", None)],
    "paint_color": [st.session_state.get("color_coche", None)],
    "state": [st.session_state.get("siglas_estado", None)]
}

df_input = pd.DataFrame(data);

# Mostrar el DataFrame con los valores ingresados
st.write("Datos ingresados para la predicción:", df_input)

# Cargar los encoders previamente guardados
encoders = cargar_encoders();

# Identificar las columnas categóricas en df_input
categorical_cols = df_input.select_dtypes(include=["object"]).columns.tolist();



# Aplicar el LabelEncoder a las columnas categóricas en df_input
for column in categorical_cols:
    # Usamos el diccionario de encoders y el método .get para aplicar el encoder correspondiente
    df_input[column] = df_input[column].apply(lambda x: encoders[column].transform([x])[0] if x in encoders[column].classes_ else -1)


# hacer un apply con el diccionario de los encoders (.get(nombre columna) y luego el metodo )
# Botón para realizar la predicción
if st.button("Realizar Predicción"):

    # Realizar la predicción
    prediccion = modelo.predict(df_input)
    prediccion_original = np.exp(prediccion);
    
    # Mostrar el resultado
    st.success(f"El valor estimado del coche es: ${prediccion_original[0]:.0f}")


# # # # #  FIN TASADOR PARTICULAR  # # # # #