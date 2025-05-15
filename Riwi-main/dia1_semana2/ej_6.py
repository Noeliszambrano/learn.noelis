hora=int(input("Ingrese la hora (0-23) "))

if hora<12 and hora>18:
    print("No es hora de trabajar")
else:
    print("Es hora de trabajar")