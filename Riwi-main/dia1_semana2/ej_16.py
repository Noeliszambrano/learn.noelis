Lista=[2,5,6,7,53,8,3,321,58,34,24,1,9,]

num=int(input("Ingrese el número a buscar "))

if num in Lista:
    pos=Lista.index(num)
    print(f"El número {num} está en la posición {pos} ")
else:
    print(f"El número {num} no está en la lista")