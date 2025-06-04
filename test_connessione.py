from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    models = client.models.list()
    print("✅ Connessione riuscita. Modelli disponibili:")
    for model in models.data:
        print("-", model.id)
except Exception as e:
    print("❌ Errore:", e)