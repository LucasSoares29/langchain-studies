import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

openai_key = os.getenv('OPENAI_API_KEY')

system_prompt = """
                    Você é um expert em línguas. Seu objetivo é a partir de uma frase em Português, traduza para inglês e espanhol.
                    Frase do usuário: {frase}
"""

# O template do prompt contém tanto o prompt quanto as variáveis de entrada em uma chave. Coloque-as em uma lista
prompt_template = PromptTemplate(input_variables=["frase"],
                                 template=system_prompt)

# Iniciar o modelo
llm = ChatOpenAI(temperature=0,
                 model_name="gpt-4o-mini")

# Montar o pipeline com o template do prompt e o modelo
chain = prompt_template | llm

# chamar o modelo
response = chain.invoke(input={"frase": "Aprender Langchain é mamão com açúcar"})

# imprimir a resposta
print(response.content)



