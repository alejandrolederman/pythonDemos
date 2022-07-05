divisas = {
    "euro" :"€",
    "peso" : "$",
    "dolar" :  "USD"  
}

divisa = input("ingrse una divisa: ")

if(divisas.get(divisa)):
    print(divisas.get(divisa))
else:
    print("divisa no encontrada")