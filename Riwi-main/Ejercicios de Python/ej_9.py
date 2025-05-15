fecha = int(input("Digite un año: "))

if fecha % 4 == 0 and fecha % 100 != 0 or fecha % 400 == 0:
    print(f"{fecha} es un año bisiesto")
else:
    print(f"{fecha} no es un año bisiesto")