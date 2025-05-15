def separar_pares_impares(lista):
  pares = []
  impares = []
  for numero in lista:
    if numero % 2 == 0:
      pares.append(numero)
    else:
      impares.append(numero)
  return pares, impares

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar_pares_impares(lista_original)
print("Lista original:", lista_original)
print("Lista de pares:", pares)
print("Lista de impares:", impares)