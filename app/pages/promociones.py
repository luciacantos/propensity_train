import streamlit as st
from utils.helpers import obtener_datos_usuario

st.title("🔥 Promociones Personalizadas")

usuario = obtener_datos_usuario()
st.write("🎯 Ofertas solo para ti:")
for promo in usuario["promociones"]:
    st.markdown(f"- **{promo}**")


st.markdown("---")
st.write("¡Aprovecha estas promociones antes de que terminen! ⏳")
