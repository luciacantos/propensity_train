import streamlit as st

st.set_page_config(page_title="Contacto y Soporte", layout="wide")

# Encabezado principal
st.title("📞 Contacto y Soporte")
st.write("¿Tienes dudas sobre el programa de beneficios? ¡Estamos aquí para ayudarte!")

# Sección de contacto directo
st.subheader("📬 Contacto")
col1, col2 = st.columns(2)
with col1:
    st.write("📧 **Email:** soporte@empresa.com")
    st.write("📱 **Teléfono:** +34 600 123 456")
with col2:
    st.write("🏢 **Dirección:** Calle Principal 123, Madrid, España")
    st.write("⏰ **Horario:** Lunes a Viernes, 9:00 - 18:00")

st.markdown("---")

# Formulario de contacto
st.subheader("✉️ Envíanos un mensaje")
with st.form(key="contact_form"):
    nombre = st.text_input("Nombre")
    email = st.text_input("Correo electrónico")
    mensaje = st.text_area("Mensaje")
    submit_button = st.form_submit_button("Enviar")

    if submit_button:
        if nombre and email and mensaje:
            st.success(f"Gracias, {nombre}. Tu mensaje ha sido enviado con éxito. 📩")
        else:
            st.error("Por favor, completa todos los campos.")

# Mapa de ubicación (simulado con imagen)
st.subheader("📍 Nuestra Ubicación")
st.image("https://maps.googleapis.com/maps/api/staticmap?center=Madrid,España&zoom=12&size=600x300&maptype=roadmap", caption="Estamos en Madrid, España")

st.markdown("---")

# Redes sociales
st.subheader("🌍 Síguenos en redes sociales")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/empresa)")
with col2:
    st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/empresa)")
with col3:
    st.markdown("[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=twitter&logoColor=white)](https://www.twitter.com/empresa)")

st.write("📢 ¡Síguenos para enterarte de las últimas novedades!")
