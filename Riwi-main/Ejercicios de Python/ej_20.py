filas = int(input("Ingrese la altura de la pirámide: "))
for i in range(1, filas + 1):
    print(" " * (filas - i), end="")
    for j in range(1, i + 1):
        print("*", end="*")
    print()