import os
import openai
from dotenv import load_dotenv

# Carica le variabili dal file .env
load_dotenv()

# Imposta chiavi e contesto del progetto
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG_ID")
openai.project = os.getenv("OPENAI_PROJECT_ID")

MODEL = "gpt-4"

def chat():
    print("🤖 Chatbot attivo! Digita 'exit' per uscire.\n")
    messages = [{"role": "system", "content": "Sei un assistente amichevole e competente."}]

    while True:
        user_input = input("👤 Tu: ")

        if user_input.lower() == "exit":
            print("👋 Uscita dalla chat.")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = openai.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            print("🤖 AI:", reply.strip())
            messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("❌ Errore:", e)
            break

if __name__ == "__main__":
    chat()
