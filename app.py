import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Carica variabili da .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Confidente 🤖")
st.write("Benvenuto! Qui parlerai con un assistente AI motivazionale.")

# Stato conversazione
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Sei un motivatore positivo ed empatico."}
    ]

# Input utente
prompt = st.text_input("Scrivi qualcosa:")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages,
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.write(f"🤖 **Risposta:** {reply}")
    except Exception as e:
        st.error(f"Errore: {e}")







