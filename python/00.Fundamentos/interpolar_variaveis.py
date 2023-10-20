# old style %

nome = "Ozzy"
idade = 31
profissão =  "supervisor de BI"
linguagem = "python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s da DIO." % (nome, idade, profissão, linguagem))

# metodo format 

nome = "Ozzy"
idade = 31
profissão =  "supervisor de BI"
linguagem = "python"
saldo = 45.433

pessoa = {"nome": "Ozzy", "idade": 31, "profissão": "Supervisor de BI", "linguagem": "Python"}

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de %{} da DIO.".format(nome, idade, profissão, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0} da DIO.".format(linguagem, profissão, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissão} e estou matriculado no curso de {linguagem} da DIO.".format(nome=nome, profissão=profissão, idade=idade, linguagem=linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissão} e estou matriculado no curso de {linguagem} da DIO.".format(**pessoa))

# f-string

nome = "Ozzy"
idade = 31
profissão =  "supervisor de BI"
linguagem = "python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissão} e estou matriculado no curso de {linguagem} da DIO.".format(**pessoa))

PI =3.14159

print (f"valor de PI {PI:.2f}")
print (f"Valor de PI: {PI:10.2f}")
print(f"Saldo: {saldo}")
print(f"Saldo: {saldo:0.2f}")