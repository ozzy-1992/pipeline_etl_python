opção = -1

while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        break
    
    if numero % 2 == 0:
        continue

    

    print(numero)

for numero in range(100):
    if numero == 10:
        break

    print (numero, end="")

for numero in range(100):
    if numero % 2 == 0:
        continue

print (numero, end="")
