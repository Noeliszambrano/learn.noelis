def es_par_o_impar(numero):
    if numero % 2 == 0:
        return f"{numero} es un número par."
    else:
        return f"{numero} es un número impar."
numero = int(input("Ingresa un número: "))
resultado = es_par_o_impar(numero)
print(resultado)