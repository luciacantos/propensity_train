import streamlit as st

st.set_page_config(page_title="Programa de Fidelidad", layout="wide")

# Encabezado principal
st.title(" Bienvenido al Programa de Fidelidad")



# Explicación de niveles y beneficios
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

# Testimonios (usando expander)
st.subheader("💬 Testimonios de clientes")
with st.expander("🌟 María G. (Nivel Oro)"):
    st.write("Gracias a este programa, he recibido descuentos exclusivos y acceso anticipado a nuevos modelos.")

with st.expander("🌟 Pedro R. (Nivel Platino)"):
    st.write("Desde que subí a Platino, me llegan ofertas personalizadas que realmente me interesan.")

# Navegación
st.subheader("📌 Explora nuestras secciones")
col1, col2 = st.columns(2)

with col1:
    if st.button("🛍️ Área Cliente"):
        st.switch_page("cliente.py")

with col2:
    if st.button("🎁 Beneficios"):
        st.switch_page("beneficios.py")

st.write("---")
st.write("📌 Usa la barra lateral para moverte entre secciones.")
