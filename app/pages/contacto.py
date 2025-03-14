import streamlit as st

def mostrar_contacto():
    st.title("Contáctanos")
    
    with st.form("contacto_form"):
        nombre = st.text_input("Nombre")
        email = st.text_input("Correo electrónico")
        mensaje = st.text_area("Mensaje")
        submit_button = st.form_submit_button("Enviar")
        
        if submit_button:
            st.success("Mensaje enviado. Te responderemos pronto.")
