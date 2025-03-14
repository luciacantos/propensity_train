import streamlit as st

st.set_page_config(page_title="Inicio - Programa de Fidelidad", layout="wide")

st.title("🎉 Bienvenido a nuestro Programa de Fidelidad 🎉")
st.write("Descubre todas las ventajas de ser parte de nuestra comunidad.")

# Niveles y beneficios
st.subheader("📊 Beneficios por niveles")
st.write("Nuestros clientes tienen acceso a diferentes niveles de beneficios dependiendo de su historial de compras.")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🥉 Nivel Básico")
    st.write("✅ Acumula puntos por cada compra")
    st.write("✅ Acceso a ofertas especiales")

with col2:
    st.subheader("🥈 Nivel Premium")
    st.write("✅ Más puntos por compra")
    st.write("✅ Descuentos exclusivos")
    st.write("✅ Prioridad en lanzamientos")

with col3:
    st.subheader("🥇 Nivel Élite")
    st.write("✅ Mayor acumulación de puntos")
    st.write("✅ Eventos VIP")
    st.write("✅ Asesoramiento exclusivo")

# Redirección al área cliente
st.sidebar.title("🔍 Navegación")
st.sidebar.page_link("pages/cliente.py", label="Área Cliente")

st.sidebar.write("---")
st.sidebar.write("🔗 Otras Secciones:")
st.sidebar.page_link("pages/beneficios.py", label="Beneficios")
st.sidebar.page_link("pages/promociones.py", label="Promociones")
st.sidebar.page_link("pages/contacto.py", label="Contacto")


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
