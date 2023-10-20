curso = 'pYtHoN'

print (curso.upper())
print (curso.lower())
print (curso.title())
print (curso.center(20))
print (curso.center(20,"#"))
print (".".join(curso))

texto  = "  curso python  "
print (texto)
print (texto.strip() + ".")
print (texto.lstrip() + ".")
print (texto.rstrip() + ".")

for letra in texto:
    print(letra, end="-")
print()
print ("-".join(texto))
 