numero = int(input("Introduce un número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("El número es múltiplo de 3 y 5")
elif numero % 3 == 0:
    print("El número es múltiplo de 3")
elif numero % 5 == 0:
    print("El número es múltiplo de 5")
else:
    print("El número no es múltiplo de 3 ni de 5")