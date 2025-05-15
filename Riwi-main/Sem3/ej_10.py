def es_palindromo(texto):

  texto = texto.replace(" ", "").replace(",", "").replace(".", "")

  texto = texto.lower()

  return texto == texto[::-1]

texto = "Anita lava la tina"
if es_palindromo(texto):
  print(f"'{texto}' es un palíndromo")
else:
  print(f"'{texto}' no es un palíndromo")