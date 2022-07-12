nombre =  input("ingresa tu nombre: ")
apellido = input("ingresa tu apellido: ")
edad = input("ingresa tu edad: ")

# datos = {
#     "nombre": nombre,
#     "apellido": apellido,
#     "edad": edad
# }

datos1 = dict(nombre = nombre, apellido = apellido, edad =  edad)
print(f"Tu nombre es {datos1['nombre']} , tu apellido es {datos1['apellido']}, tu edad es {datos1['edad']}")
# print("el precio de las frutilla es  ,frutas")

# frutas = {
#     "pera" : 120,
#     "manzana" : 200,
#     "durazno" : 150,
#     "banana" : 230
# }

# fruta = input("Ingrese una fruta: ")

# if (frutas.get(fruta)):
#     kilos = float(input("Ingrese la cantidad de kilos que desea comprar: "))
#     total = kilos * frutas[fruta]
#     print(f"La fruta a compra es {fruta} {frutas[fruta]}  por {kilos} kgs y el total es ${total}")
# else:
#     print("La fruta ingresada no existe")
    
# print(frutas.items())
