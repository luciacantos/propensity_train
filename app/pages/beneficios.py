import streamlit as st

def mostrar_beneficios(df):
    st.title("Beneficios para Clientes")
    
    # Gráfico de distribución de clientes por segmento
    st.subheader("Distribución de Clientes por Segmento")
    segment_counts = df["Segmento"].value_counts()
    st.bar_chart(segment_counts)
    
    # Explicación de beneficios
    beneficios = {
        "Muy baja": "Sin beneficios asignados.",
        "Baja": "Emails con promociones leves.",
        "Media": "Acceso a descuentos y promociones.",
        "Alta": "Beneficios exclusivos y soporte premium.",
        "Muy alta": "Acceso VIP a eventos y mejores precios."
    }

    segmento = st.selectbox("Selecciona un segmento:", list(beneficios.keys()))
    st.write(f"**Beneficios para clientes {segmento}:** {beneficios[segmento]}")
