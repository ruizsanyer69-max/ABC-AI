import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ABC AI", page_icon="😎")
st.markdown("<center><h1>😎 A B C</h1></center>", unsafe_allow_html=True)

# Configuración segura de la API
if "GOOGLE_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # Usamos el nombre de modelo más compatible
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Dile algo a ABC..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                # Aquí pedimos la respuesta
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Hubo un detalle: {e}")
else:
    st.warning("Revisa tus Secrets en Streamlit.")
