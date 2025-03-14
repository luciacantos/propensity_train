import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Configuración de la página
st.set_page_config(page_title="📊 Análisis de Clientes de Coches", layout="wide")

# Función para cargar datos
@st.cache_data
def cargar_datos():
    ruta_csv = os.path.join("data", "Propensity_Processed.csv")  # Ajustado a tu estructura
    return pd.read_csv(ruta_csv)

# Cargar los datos
df = cargar_datos()

# Título
st.title("📊 Análisis de Clientes de Coches")

# Mostrar tabla de datos
st.subheader("📋 Datos de Clientes")
st.dataframe(df)

# Boxplot de Coste Venta por Segmento
st.subheader("📊 Boxplot de Coste Venta por Segmento")
fig, ax = plt.subplots()
sns.boxplot(x=df["Segmento_Cliente"], y=df["COSTE_VENTA"], palette="viridis", ax=ax)
st.pyplot(fig)

# Matriz de correlaciones
st.subheader("🔗 Matriz de Correlaciones")
fig, ax = plt.subplots()
sns.heatmap(df[["COSTE_VENTA", "km_anno"]].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# Scatter plot
st.subheader("📈 Relación entre Coste Venta y KM Año")
fig, ax = plt.subplots()
sns.scatterplot(x=df["COSTE_VENTA"], y=df["km_anno"], hue=df["Segmento_Cliente"], palette="viridis", alpha=0.6, ax=ax)
st.pyplot(fig)
