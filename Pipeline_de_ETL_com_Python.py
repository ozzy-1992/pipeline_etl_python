#Extract

import pandas as pd
import requests

def gerar_mensagem(cliente):
    UserId = cliente['UserId']
    nome = cliente['nome']
    idade = cliente['idade']
    saldo = cliente['saldo']
    tem_cartao = cliente['cartao_crédito']
    limite = cliente['limite_conta']
    
    if idade < 18:
        return f"Olá {nome}, sabia que temos uma conta universitária perfeita para você? É o jeito ideal de começar a investir no seu futuro!"
    
    mensagem = f"Olá {nome},"
    
    if saldo < 2500:
        mensagem += " vimos que você tem um saldo moderado. Já pensou em começar a investir em uma poupança?"
    else:
        mensagem += " que tal diversificar seus investimentos e fazer seu dinheiro render ainda mais?"
        
    if not tem_cartao and idade >= 18:
        mensagem += " Além disso, notamos que você ainda não tem um cartão de crédito conosco. Que tal aproveitar nossas ofertas exclusivas?"
    
    return mensagem


file_path = "C:\\Users\\vinic\\OneDrive\\Documentos\\Coding\\SDW2023.csv"

#Tratamento
## Lendo o arquivo
try:
    data = pd.read_csv(file_path)
    print("Dados carregados com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")
    exit()

# Gerar mensagens para cada cliente
mensagens = []
for index, cliente in data.iterrows():
    mensagem = gerar_mensagem(cliente)
    mensagens.append(mensagem)

# Imprimir mensagens geradas
print("Mensagens geradas:")
for msg in mensagens:
    print(msg)


#Carregar 

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['UserId']}", json=user)
    return True if response.status_code == 200 else False

# Gerando mensagens e atualizando usuários
for index, cliente in data.iterrows():
    user = cliente.to_dict()
    userID = cliente['UserId']
    user['marketing_message'] = gerar_mensagem(cliente)  # Gerando a mensagem de marketing
    
    success = update_user(user)
    print(f"User {user['nome']} (ID: {user['UserId']}) updated? {success}!")

