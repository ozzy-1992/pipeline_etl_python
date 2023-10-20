a = int(input("number: "))
print(a)

a += 1
print(a)

a += 1
print(a)

texto = input("texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else: 
    print()
    print("Razô")


