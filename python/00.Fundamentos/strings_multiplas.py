#strings múltiplas ou triplas

nome = 'Vinicius Oziel'
curso = 'Python'

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo {curso}
"""

mensagem1 = f'''
    Olá meu nome é {nome},
Eu estou aprendendo {curso}
        Aplicando o Recuo
''' 

print(mensagem)
print(mensagem1)

print('''
      ######## Menu ######
      
      1 - Depositar
      2 - sacar
      3 - Sair
      
      ####################

        Now, sashay, away!!!
      '''
)