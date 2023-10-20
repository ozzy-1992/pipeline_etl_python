conta_normal = False
conta_universitária = True

saldo = 2000
saque = int(input("valor: "))
cheque_especial = 500

if conta_normal:
    if saldo>=saque:
        print("saque realizado")
    elif saque<= (saldo + cheque_especial):
        print("caiu no cheque. vc nos deve: R$", (saldo+cheque_especial)-(saque+cheque_especial))
    else:
        print("Sashay away")    
elif conta_universitária:
    if saldo >= saque:
        print("saque realizado")
    else: 
        print("sashay away")

print ("sobrou: R$ ", saldo-saque)               
print("valeu!")