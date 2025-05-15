def guardar_y_encontrar_maximo(valores):
  if not valores:
    return None
  return max(valores)
mis_valores = [5, 2, 8, 1, 9, 3]
valor_maximo = guardar_y_encontrar_maximo(mis_valores)
if valor_maximo is not None:
  print("El valor máximo en la lista es:", valor_maximo)
else:
  print("La lista está vacía.")