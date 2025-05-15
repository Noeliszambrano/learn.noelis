def factorial(numero):

  if numero < 0:
    return None  
  elif numero == 0:
    return 1  
  else:
    resultado = 1
    for i in range(1, numero + 1):
      resultado *= i
    return resultado


while True:
  try:
    numero = int(input("Ingresa un número entero positivo: "))
    break 
  except ValueError:
    print("La entrada debe ser un número entero.")


factorial_resultado = factorial(numero)


if factorial_resultado is not None:
  print(f"El factorial de {numero} es {factorial_resultado}")
else:
  print("No se puede calcular el factorial de números negativos.")