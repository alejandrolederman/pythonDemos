asistencia = int (input("indique porsentaje de asistencia:  %"))
nota1 = int(input("nota del primer examen: "))
nota2 = int(input("nota del segundo examen: "))
nota3 = int(input("nota del tercer examen: "))

promedio = (nota1 + nota2 + nota3) / 3

print (promedio)

if ((promedio <= 8) and (asistencia< 80)):
    print ("promocionaste")
else:
    print("sera el proximo año :(")