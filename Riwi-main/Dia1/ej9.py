fecha = int(input("digita un año"))
if fecha%4 == 0 and (fecha%100 !=0) or (fecha%400 == 0):
    print("es bisisesto")
else:
    print("no es bisisesto")
    