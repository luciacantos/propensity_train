import streamlit as st
import pandas as pd
import altair as alt
from utils.helpers import obtener_datos_usuario

st.set_page_config(page_title="Tus Beneficios", layout="wide")

# Obtener datos del usuario
usuario = obtener_datos_usuario()

st.title(f"🎁 Beneficios exclusivos para ti")

# Mostrar beneficios personales en una tarjeta bonita
st.subheader("🎖 Beneficios actuales")
st.success("Estos son los beneficios que has desbloqueado hasta ahora:")

for beneficio in usuario["beneficios"].split("\n"):
    if beneficio.strip():
        st.markdown(f" ✅ **{beneficio.strip()}**")

st.markdown("---")

# Simulación de progreso hacia el siguiente beneficio
puntos_actuales = usuario["puntos"]
puntos_para_extra = 5000  # Se puede cambiar según la lógica de beneficios

st.subheader("📈 Progreso hacia más beneficios")
st.write(f"Tienes **{puntos_actuales} puntos**. Al llegar a **{puntos_para_extra} puntos**, desbloquearás más recompensas.")

st.progress(puntos_actuales / puntos_para_extra)

datos_beneficios = pd.DataFrame({
    "Beneficio": ["Descuento en compras", "Acceso VIP", "Eventos privados"],
    "Puntos Acumulados": [2000, 1500, 500]
})

# Crear gráfico de barras con Altair
chart = alt.Chart(datos_beneficios).mark_bar(cornerRadius=5).encode(
    x="Puntos Acumulados:Q",
    y=alt.Y("Beneficio:N", sort="-x"),
    color=alt.value("#FFA500")
).properties(
    title="📊 Beneficios acumulados por categoría"
)

# Mensaje de motivación
if puntos_actuales >= puntos_para_extra:
    st.success("🎉 ¡Has desbloqueado un **beneficio sorpresa**! Pronto recibirás una notificación.")
else:
    st.warning(f"📢 Te faltan **{puntos_para_extra - puntos_actuales} puntos** para tu próxima recompensa.")

st.markdown("---")

# Botón de regreso a la página principal
if st.button("⬅️ Volver a Inicio"):
    st.switch_page("app.py")

