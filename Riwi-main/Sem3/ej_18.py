def sumar_unicos(lista):
    conjunto_unicos = set(lista)
    suma = sum(conjunto_unicos)
    return suma
lista_numeros = [1, 2, 3, 2, 4, 1, 5]
suma_unicos = sumar_unicos(lista_numeros)
print(f"La suma de los elementos únicos es: {suma_unicos}")