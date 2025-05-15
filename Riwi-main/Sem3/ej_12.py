def eliminar_duplicados(lista):
  nueva_lista = []
  for elemento in lista:
    if elemento not in nueva_lista:
      nueva_lista.append(elemento)
  return nueva_lista

mi_lista = [1, 2, 3, 2, 4, 1, 5]
lista_sin_duplicados = eliminar_duplicados(mi_lista)
print(lista_sin_duplicados)