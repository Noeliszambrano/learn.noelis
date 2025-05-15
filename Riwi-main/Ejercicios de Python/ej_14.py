numero = int(input("Digite un numero: "))
for i in range (0,11):
    resultado = i * numero
    print(("%d * %d = %d") % (numero, i, resultado))