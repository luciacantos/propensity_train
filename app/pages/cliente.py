import streamlit as st
from utils.helpers import obtener_datos_usuario

st.title("👤 Área Cliente")

usuario = obtener_datos_usuario()

st.sidebar.title(f"📌 {usuario['nombre']}")
st.sidebar.write(f"🎖 Nivel: **{usuario['nivel']}**")

st.metric("📊 Puntos Acumulados", usuario["puntos"])
st.metric("💰 Total Gastado", f"${usuario['dinero_gastado']}")

st.write("🔹 Tus Beneficios Actuales:")
st.markdown(usuario["beneficios"])

st.markdown("---")
st.write("¡Sigue comprando para alcanzar el Nivel Élite! 🎉")

