


import streamlit as st
from utils.helpers import clasificar_cliente
import pandas as pd
import joblib

# Configurar la app
st.set_page_config(page_title="Estrategia de Marketing", layout="wide")

# Cargar modelo y datos
modelo = joblib.load("models/modelo_gradient_boosting.pkl")
df = pd.read_csv("data/stg/Propensity_input.csv", index_col=0)

# Calcular probabilidades
df["Propension_Compra"] = modelo.predict_proba(df)[:, 1]
df["Segmento"] = df["Propension_Compra"].apply(clasificar_cliente)

# Sidebar con navegación
st.sidebar.title("Menú")
pagina = st.sidebar.radio("Selecciona una página:", ["Inicio", "Área Cliente", "Beneficios", "Promociones", "Contacto"])

# Redirigir a la página seleccionada
if pagina == "Inicio":
    st.title("Estrategia de Marketing Basada en Probabilidad de Compra")
    st.write("Bienvenido a la plataforma de análisis de clientes.")
    st.image("assets/marketing_strategy.png")  # Imagen opcional
elif pagina == "Área Cliente":
    from pages import cliente
    cliente.mostrar_cliente(df)
elif pagina == "Beneficios":
    from pages import beneficios
    beneficios.mostrar_beneficios(df)
elif pagina == "Promociones":
    from pages import promociones
    promociones.mostrar_promociones(df)
elif pagina == "Contacto":
    from pages import contacto
    contacto.mostrar_contacto()
