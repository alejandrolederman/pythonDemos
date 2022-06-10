nivel = int (input("indique si nivel: "))
tarjeta = input("indique marca de su tarjeta: ")

if((nivel == 5) and (tarjeta == "Visa")):
    print("puede acceder al descuento")

else:
    print("no aceptado")