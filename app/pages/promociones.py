import streamlit as st

def mostrar_promociones(df):
    st.title("Promociones Personalizadas")
    
    # Lista de promociones por segmento
    promociones = {
        "Muy baja": "Sin promociones asignadas.",
        "Baja": "Descuento del 5% en la próxima compra.",
        "Media": "Oferta 2x1 en productos seleccionados.",
        "Alta": "Acceso a eventos privados y 10% de descuento.",
        "Muy alta": "Descuentos exclusivos y acceso VIP a lanzamientos."
    }

    segmento = st.selectbox("Selecciona un segmento:", list(promociones.keys()))
    st.write(f"**Promociones para clientes {segmento}:** {promociones[segmento]}")
