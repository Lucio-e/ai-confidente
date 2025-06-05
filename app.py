import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Confidente 🤖")
st.write("Benvenuto! Qui parlerai con un assistente AI motivazionale.")

# Inizializza lo stato della sessione
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Sei un motivatore positivo ed empatico. Dai risposte brevi, chiare e incoraggianti."}
    ]

# Input utente
user_input = st.text_input("Scrivi qualcosa:")

if user_input:
    # Aggiungi messaggio dell’utente
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )

        reply = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.markdown(f"🧠 **Risposta:** {reply}")

    except Exception as e:
        st.error(f"Errore: {e}")





