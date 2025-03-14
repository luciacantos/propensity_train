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


