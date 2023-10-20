# And = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser true


print(True and True)
print(True and False)
print (False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 200
saque_2 = 1200
limite = 100
lis = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

exp_3 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque_2)
print(exp_3)

(saldo >= saque and saque <=limite)
(saldo >= saque or saque <=limite)
(saldo + lis >= saque)

