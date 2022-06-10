edad = int(input("cual es su edad? "))

if (edad <= 3):
    print ("puede entrar gratis")
elif (edad >= 4 and edad <= 18):
    print ("debe pagar 5")
elif (edad > 19):
    print("debe pagar 10")
    