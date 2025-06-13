import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key
)

lista_perguntas = [
    "Quero visitar um lugar no Brasil, famoso por praias e cultura. Pode sugerir?",
    "Qual a melhor época do ano para ir?"
]

for uma_pergunta in lista_perguntas:
    resposta = modelo.invoke(uma_pergunta)
    print("Usuário: ", uma_pergunta),
    print("IA: ", resposta.content, "\n")