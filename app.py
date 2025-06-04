import streamlit as st
import openai

# Chiavi prese in automatico dai secrets di Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]
openai.organization = st.secrets["OPENAI_ORG_ID"]

st.title("AI Confidente 🤖")
st.write("Benvenuto! Qui parlerai con un assistente AI motivazionale.")

prompt = st.text_input("Scrivi qualcosa:")

if prompt:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sei un motivatore positivo ed empatico."},
                {"role": "user", "content": prompt}
            ]
        )
        st.write("💬 **Risposta:**", response.choices[0].message["content"])
    except Exception as e:
        st.error(f"Errore: {e}")


