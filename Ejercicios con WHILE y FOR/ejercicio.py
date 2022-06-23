# Escriba un programa que solicite una contraseña y la vuelva a solicitar hasta que
# # las dos contraseñas coincidan.

from tabnanny import check

pasword = str (input("ingrerse una contraseña: "))

confirmacion = str(input("vuelva a ingresar la contraseña: "))

while pasword != confirmacion:
    confirmacion = str(input("vuelva a ingresar la contraseña: "))

else:
    print("la contraseña coincide")
    