def verificacion ( letra):
    
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra =="u"):
        if (letra == "i" or letra == "u"):
            return "es una vocal abierta"
        else:
            return "es vocal cerrada"
    else:
        return "es consonante"
 
        
letraNueva = str(input("iingese una letra: "))

print(verificacion(letraNueva))