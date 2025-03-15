import streamlit as st
import pandas as pd

st.set_page_config(page_title="Beneficios", layout="wide")

st.title("🎁 Tus Beneficios")

# Simulación de datos de beneficios
datos = {
    "Nivel": ["Básico", "Plata", "Oro", "Platino"],
    "Descuentos (%)": [5, 10, 15, 20],
    "Acceso VIP": [False, True, True, True],
    "Puntos Extra": [0, 50, 100, 200]
}

df = pd.DataFrame(datos)

# Tabs para mostrar beneficios por categoría
tab1, tab2, tab3 = st.tabs(["💰 Descuentos", "🔝 Beneficios Exclusivos", "📊 Evolución"])

with tab1:
    st.write("A medida que subes de nivel, obtienes más descuentos:")
    st.bar_chart(df.set_index("Nivel")["Descuentos (%)"])

with tab2:
    st.write("Beneficios adicionales por cada nivel:")
    st.dataframe(df)

with tab3:
    st.write("Comparación de beneficios en cada nivel")
    st.line_chart(df.set_index("Nivel")["Puntos Extra"])

# Motivación: cuánto falta para el siguiente nivel
nivel_actual = "Plata"
puntos_actuales = 300
puntos_requeridos = 500

st.write("---")
st.subheader("📈 ¿Cuánto te falta para mejorar de nivel?")
st.write(f"Actualmente eres **{nivel_actual}**. Necesitas {puntos_requeridos - puntos_actuales} puntos más para subir a Oro.")

# Botón de regreso
if st.button("⬅️ Volver a Inicio"):
    st.switch_page("app.py")
