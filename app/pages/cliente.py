import streamlit as st

def mostrar_cliente(df):
    st.title("Área Cliente")
    
    # Selección de cliente
    cliente_seleccionado = st.selectbox("Selecciona un cliente:", df.index)
    
    # Mostrar detalles del cliente
    cliente_info = df.loc[cliente_seleccionado]
    st.write(f"**Probabilidad de compra:** {cliente_info['Propension_Compra']:.2f}")
    st.write(f"**Segmento:** {cliente_info['Segmento']}")

    # Explicación según segmento
    estrategias = {
        "Muy baja": "No se aplican estrategias de marketing en este grupo.",
        "Baja": "Envío de emails con ofertas leves para incentivar la compra.",
        "Media": "Se ofrecen descuentos y programas de fidelidad.",
        "Alta": "Acceso a beneficios exclusivos y mejores precios.",
        "Muy alta": "Clientes premium con recompensas especiales y eventos VIP."
    }
    st.info(estrategias[cliente_info["Segmento"]])
