import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Confidente 🤖")
st.write("Benvenuto! Qui parlerai con un assistente AI motivazionale.")

prompt = st.text_input("Scrivi qualcosa:")

if prompt:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sei un motivatore positivo ed empatico."},
                {"role": "user", "content": prompt}
            ]
        )
        st.write("🤖 **Risposta:**", response.choices[0].message.content)
    except Exception as e:
        st.error(f"Errore: {e}")




