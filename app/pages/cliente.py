import streamlit as st
import pandas as pd

st.set_page_config(page_title="Área Cliente", layout="wide")

# Simulación de datos dinámicos
usuario = "Juan Pérez"
nivel = "Plata"
puntos = 300
proximo_nivel = 500
compras = [
    {"Producto": "Coche Sedán 2022", "Fecha": "2024-02-15", "Precio": "$25,000"},
    {"Producto": "Seguro Premium", "Fecha": "2024-03-01", "Precio": "$1,200"},
    {"Producto": "Mantenimiento Anual", "Fecha": "2024-03-10", "Precio": "$300"}
]

# Cabecera
st.title(f"👋 Bienvenido, {usuario} ({nivel})")

# Barra de progreso de nivel
st.subheader("🏆 Tu progreso hacia el siguiente nivel")
st.progress(puntos / proximo_nivel)
st.write(f"🔹 Te faltan **{proximo_nivel - puntos} puntos** para subir a **nivel Oro**.")

# Beneficios desbloqueados
if puntos >= 250:
    st.success("🎉 ¡Has desbloqueado un **descuento especial** en tu próxima compra!")

# Historial de compras con tabla interactiva
st.subheader("📜 Historial de Compras")
df_compras = pd.DataFrame(compras)
st.dataframe(df_compras, use_container_width=True)

# Análisis de puntos ganados por compra
st.subheader("📊 Puntos ganados por compra")
df_compras["Puntos Ganados"] = [150, 100, 50]
st.bar_chart(df_compras.set_index("Producto")["Puntos Ganados"])

# Sección de Recomendaciones Personalizadas
st.subheader("🔍 Recomendaciones para ti")
opciones = {
    "Seguro extendido": "Protege tu coche por 2 años adicionales.",
    "Accesorios exclusivos": "Llantas de lujo y asientos personalizados.",
    "Mantenimiento preferente": "Servicio express sin costo adicional."
}
recomendacion = st.selectbox("Selecciona una recomendación:", list(opciones.keys()))
st.write(f"✨ Beneficio especial: **{opciones[recomendacion]}**.")

# Botón de regreso
st.write("---")
if st.button("⬅️ Volver a Inicio"):
    st.switch_page("app.py")

