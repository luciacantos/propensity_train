import streamlit as st
from utils.helpers import obtener_datos_usuario
import datetime

st.set_page_config(page_title="Promociones Personalizadas", layout="wide")

# Obtener datos del usuario
usuario = obtener_datos_usuario()

st.title(f"🔥 Promociones Exclusivas para ti")

# Mostrar un mensaje especial si tiene descuentos destacados
if "Descuento especial en tu próxima compra" in usuario["promociones"]:
    st.success("🎉 ¡Tienes un **descuento especial** disponible! No lo dejes pasar.")

st.subheader("Ofertas solo para ti")
st.write("Aprovecha estas promociones antes de que terminen:")

# Dividir las promociones en tarjetas
col1, col2 = st.columns(2)

for i, promo in enumerate(usuario["promociones"]):
    with col1 if i % 2 == 0 else col2:
        st.markdown(
            f"""
            <div style='background-color:#ffcc00;padding:15px;border-radius:10px;margin-bottom:10px;'>
                <h4 style='color:black;'>🔥 {promo['titulo']}</h4>
                <p style='color:black;'>{promo['descripcion']}</p>
                <p style='color:black;'>⏳ Oferta válida hasta <b>{promo['fecha_expiracion'].strftime('%d/%m/%Y')}</b></p>
            </div>
            """, unsafe_allow_html=True
        )


st.markdown("---")

# Mostrar cuenta regresiva para promociones activas
st.subheader("⏳ Tiempo restante para aprovechar tus promociones")
fecha_fin = datetime.datetime.now() + datetime.timedelta(days=7)
dias_restantes = (fecha_fin - datetime.datetime.now()).days
st.metric(label="Días restantes", value=f"{dias_restantes} días")

st.write("¡No dejes pasar estas ofertas! 🚀")
