from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Sei un motivatore positivo ed empatico"},
        {"role": "user", "content": prompt}
    ]
)

st.write("🤖 **Risposta:**", response.choices[0].message.content)



