peso = float(input("Digite su peso"))
altura = float(input("Digite su altura"))
imc = (peso /(altura*altura))
if imc < 18.4:
    print("Bajo peso")
if 18.5>= imc <=24.9:
    print("normal")
if 25>= imc <=29.9:
    print("SOBREPESO")
if imc >30:
    print("OBESO")


