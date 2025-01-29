import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage, StrOutputParser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to generate chatbot responses
def get_chat_response(user_input, chat_history, llm):
    """
    Recebe como parâmetros de entrada a mensagem do usuário (user_input), o histórico de chat
    num formato de lista [HumannMessage(), AIMessage(),...] e também a llm que será usado neste
    chatbot
    
    Se eu quiser usar mais de um chatbot, consigo usar o terceiro parâmetro llm para trocar o llm
    e aproveitar a fução
    """
    messages = [SystemMessage(content="""Seu nome é AIBot. 
                              Você um chatbot que tem que resolver as dúvidas 
                              das pessoas da forma mais amigável possível""")]
    
    # Carrega o contexto da história nna lista de mensagens acima
    for human, ai in chat_history:
        messages.append(HumanMessage(content=human))
        messages.append(AIMessage(content=ai))
    
    # Insere a mensagem do usuário no final
    messages.append(HumanMessage(content=user_input))
    
    chain = llm | StrOutputParser()

    response = chain.invoke(messages)
    return response

