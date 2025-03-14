import streamlit as st
from utils.helpers import obtener_datos_usuario

st.title("🎁 Tus Beneficios")

usuario = obtener_datos_usuario()
st.write(f"📌 Tu nivel: **{usuario['nivel']}**")
st.write("Estos son los beneficios exclusivos para ti:")
st.markdown(usuario["beneficios"])


st.write("Sube de nivel y accede a más recompensas 🚀")

