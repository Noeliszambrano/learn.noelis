def eliminar_duplicados(lista):
    conjunto = set(lista)
    lista_sin_duplicados = list(conjunto)
    return lista_sin_duplicados

mi_lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = eliminar_duplicados(mi_lista)
print(lista_sin_duplicados)