# 4. Realiza un programa que pida 2 números enteros, e imprima los números pares
# que existen entre los 2.

numero1 = int(input("ingrese un numero: "))
numero2 =  int(input("ingrese un numero mayor al anterior: "))

for i in range (numero1, numero2):
    if (i % 2 == 0):
        print (i)
    