
mi_lista = [10, 20, 30, 40, 50]
elemento_buscado = int(input("Digite un numero"))
encontrado = False
for elemento in mi_lista:
    if elemento == elemento_buscado:
        print("Elemento encontrado:", elemento)
        encontrado = True
        break
      
if not encontrado:
    print("Elemento no encontrado en la lista")