numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

if numero1 > numero2:
    if numero1 > numero3:
        mayor = numero1
    else:
        mayor = numero3
else:
    if numero2 > numero3:
        mayor = numero2
    else:
        mayor = numero3

print("El número más grande es:", mayor)