import matematicas.funcionesBasicas as funcBasic
import matematicas.funcionesComplejas as funComplex

numero_a = int(input("ungrese un numero a: "))
numero_b = int(input("ungrese un numero b: "))

numero_c = int(input("ungrese un numero c: "))
numero_d = int(input("ungrese un numero d: "))

print (funcBasic.suma(numero_a, numero_b))
print (funcBasic.restar(numero_a, numero_b))

print(funComplex.multiplicas(numero_c, numero_d))
print(funComplex.dividir(numero_c, numero_d))


