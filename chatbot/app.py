import streamlit as st
import subprocess
import time
from langchain_openai import ChatOpenAI
from langchain_ollama.llms import OllamaLLM
from chatbot import get_chat_response
from streamlit_chat import message

"""
É necessário instalar o Llama na máquina local para executar este app em ollama.com
"""

def executar_llama():
    # Comando a ser executado
    command = "ollama run llama3.2"

    # Executa o comando no prompt de comando do Windows
    process = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Exibe a saída do comando
    print("Saída:", process.stdout)
    print("Erro:", process.stderr)


# Initialize OpenAI Chat Model
llm = ChatOpenAI(temperature=0.8,
                 model_name="gpt-4o-mini")

llm_llama = OllamaLLM(model="llama3.2")

executar_llama()

st.set_page_config(page_title="AIBot Chat", layout="wide")

st.title("🤖 AIBot - Seu Assistente Inteligente")

if "chat_history_llm1" not in st.session_state:
    st.session_state.chat_history_llm1 = []
if "chat_history_llm2" not in st.session_state:
    st.session_state.chat_history_llm2 = []

user_input = st.text_input("Pergunte algo:", "")

col1, col2 = st.columns(2)

with col1:
    enviar = st.button("Enviar")

with col2:
    reiniciar = st.button("🔄 Recarregar Página")


if enviar:
    if user_input:
        with st.spinner("Gerando resposta modelo 1..."):
            response = get_chat_response(user_input, st.session_state.chat_history_llm1, llm)
            st.session_state.chat_history_llm1.append((user_input, response))
            time.sleep(1)
        with st.spinner("Gerando resposta modelo 2..."):
            response = get_chat_response(user_input, st.session_state.chat_history_llm2, llm_llama)
            st.session_state.chat_history_llm2.append((user_input, response))
            time.sleep(1)


# Carrega histórico de chat até aqui
# usamos zip aqui para que ficasse sincronizado as duas listas e eu conseguisse pegar um elemento de cada
for (human, ai_llm1), (_, ai_llm2) in zip(st.session_state.chat_history_llm1, st.session_state.chat_history_llm2):
    # st.write(f"**Você:** {human}")
    # st.write(f"**AIBot OpenAI:** {ai_llm1}")
    # st.write(f"**AIBot Llama:** {ai_llm2}")
    # st.write("---")
    message(human, is_user=True)
    message(f"OpenAI: {ai_llm1}")
    message(f"Llama3.2: {ai_llm2}")


if reiniciar:
    st.session_state.clear()
    st.rerun()