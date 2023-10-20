MAIOR_IDADE = 18
IDADE_ESPECIAL = 16


idade = int(input("INFORME SUA IDADE: "))

if idade >= MAIOR_IDADE:
    print("pode tirar")

if idade < MAIOR_IDADE:
    print("espera, viado")


if idade >= MAIOR_IDADE:
    print("pode tirar")

else:
    print("espera, viado")


if idade >= MAIOR_IDADE:
    print("pode tirar")

elif idade >= IDADE_ESPECIAL:
    print("vaza estadunidense")

else:
    print("espera, viado")

