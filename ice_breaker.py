import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser





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

# Montar o pipeline com o template do prompt e o modelo. O StrOutputParser vai acessar automaticamente o .content da resposta do modelo
chain = prompt_template | llm | StrOutputParser() 

# chamar o modelo
response = chain.invoke(input={"frase": "Aprender Langchain é mamão com açúcar"})

# imprimir a resposta
print(f"Resposta OpenAI: {response}")


####### LLAMA #########
""" Instalação: 1 - Vá em ollama.com para baixar o modelo. e instale o modelo
                2 - Vá no cmd e rode ollama run llama3.2
                3 - Quando acabar os testes, digitar /bye no prompt """

llm_llama = OllamaLLM(model="llama3.2")

chain_2 = prompt_template | llm_llama | StrOutputParser() 

response2 = chain_2.invoke(input={"frase": "Aprender Langchain é mamão com açúcar"})

print(f"Resposta Llama: {response2}")

###### Mistral #########
""" Instalação: 1 - Vá no cmd e rode ollama pull mistral """

llm_mistral = OllamaLLM(model="mistral")

chain_3 = prompt_template | llm_mistral | StrOutputParser() 

response3 = chain_3.invoke(input={"frase": "Aprender Langchain é mamão com açúcar"})

print(f"Resposta Mistral: {response3}")

with open("output_translations_models.txt", "w", encoding="utf-8") as file:
    file.write("Resposta OpenAI: ")
    file.write(response)
    file.write("\nResposta Llama: ")
    file.write(response2)
    file.write("\nResposta Mistral: ")
    file.write(response3)



