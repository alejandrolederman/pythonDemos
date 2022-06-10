edad = int (input("cual es su edad? "))
ingreso = int(input("cual es su ingreso mensual? "))

if ((edad > 16) and (ingreso > 1000)):
    print ("tiene que tributar")
else:
    print("no tiene que tributar")
