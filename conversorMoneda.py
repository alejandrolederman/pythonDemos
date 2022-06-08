from mimetypes import init


pais = input("coloque su pais: ")
dolar = int (input("cantidad de dolares: $"))

if(pais == "Argentina"):
    print ("$" + str(dolar * 200))
elif(pais == "Colombia"):
    print("$" + str(dolar * 3950))
elif(pais == "Bolivia"):
    print ("$" + str(dolar * 6.9))
else:
    print("seleccione otro pais")