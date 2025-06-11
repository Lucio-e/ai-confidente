import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Carica variabili d'ambiente
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Imposta titolo e icona
st.set_page_config(page_title="AI Confidente 🤖", page_icon="💬")

st.title("AI Confidente 🤖")
st.write("Benvenuto! Qui parlerai con il tuo assistente AI motivazionale.")

# Inizializza storico conversazione nella sessione utente
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Sei un motivatore empatico, positivo e incoraggiante. Fornisci risposte brevi, chiare e di supporto."}
    ]

# Mostra tutto lo storico visivo (come chat vera)
for message in st.session_state.messages[1:]:  # escludiamo il system prompt visivo
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo input stile chat (come ChatGPT)
if user_input := st.chat_input("Scrivi il tuo messaggio qui..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        st.error(f"Errore: {e}")

# Pulsante reset chat
if st.button("🔄 Cancella conversazione"):
    st.session_state.messages = [
        {"role": "system", "content": "Sei un motivatore empatico, positivo e incoraggiante."}
    ]
    st.rerun()










