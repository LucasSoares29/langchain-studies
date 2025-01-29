import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
openai_key = os.getenv('OPENAI_API_KEY')

#### Criando o modelo
llm = ChatOpenAI(temperature=0.8,
                 model_name="gpt-4o-mini")

#### Criando o prompt
system_prompt = """
    "Escreva uma história de até 500 caracteres sobre {assunto}"
"""
prompt_template1 = PromptTemplate(input_variables=["assunto"], 
                                  template=system_prompt)

#### Interface
st.title("Criador de contos")
assunto = st.text_input("Digite um assunto para criar um conto sobre...")
print(assunto)

#### Acesso ao modelo
if assunto:
    # Aparece um spinner para criar este conto
    with st.spinner("Criando conto..."):
        chain = prompt_template1 | llm | StrOutputParser()
        resposta = chain.invoke({"assunto": assunto})
        st.write(resposta)

