import streamlit as st  
from openai import OpenAI
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Cria o cliente OpenAI
modelo = OpenAI(api_key=api_key)

st.set_page_config(page_title="BrunoAI")
st.write("### BrunoAI - Seu chatbot inteligente")

# Memória da conversa
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []
  
# Mostrar mensagens anteriores
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

# Entrada do usuário
mensagem_usuario = st.chat_input("Escreva sua mensagem")

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": mensagem_usuario})

    # Obter resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state["lista_mensagens"]
    )

    resposta_ai = resposta_modelo.choices[0].message.content

    # Mostrar resposta da IA
    st.chat_message("assistant").write(resposta_ai)
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ai})