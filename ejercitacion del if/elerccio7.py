nombre = input("nombre del paciente: ")
temperatura = float(input("indique su temperatura: "))

if (temperatura > 37.5):
    print("la temperatura del paciente ", nombre, " tiene fiebre")
    covid = input("el alumno estuvo con un caso estrecho de covid en su familia? ")
    if (covid == "si"):
        print ("el paciente sera internado")
    else:
        print("es solo una gripe")
else:
    print("no tiene fiebre")