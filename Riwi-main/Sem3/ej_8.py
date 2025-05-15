def contar_letra_en_palabra(palabra, letra):

  return palabra.count(letra)

palabra = "Python es un lenguaje de programación"
letra = "n"
cantidad = contar_letra_en_palabra(palabra, letra)
print(f"La letra '{letra}' aparece {cantidad} veces en la palabra '{palabra}'") 
