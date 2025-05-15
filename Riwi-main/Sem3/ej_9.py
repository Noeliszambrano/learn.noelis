def obtener_pares(lista_numeros):

  lista_pares = []
  for numero in lista_numeros:
    if numero % 2 == 0:
      lista_pares.append(numero)
  return lista_pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = obtener_pares(numeros)
print(pares)