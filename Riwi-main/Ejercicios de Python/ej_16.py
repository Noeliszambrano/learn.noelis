
numero_secreto = 10
print("¡Bienvenido a Adivina el número!")
print("Estoy pensando en un número entre 1 y 20.")

while True:
    suposicion = int(input("Ingresa tu suposición: "))
    if suposicion == numero_secreto:
        print(f"¡Correcto!")
        break
    elif suposicion < numero_secreto:
        print("Demasiado bajo. Intenta un número más alto.")
    else:
        print("Demasiado alto. Intenta un número más bajo.")

print(f"El número secreto era {numero_secreto}.")