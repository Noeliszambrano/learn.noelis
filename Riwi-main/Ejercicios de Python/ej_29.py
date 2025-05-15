def encontrar_max_min(lista):
    if not lista:
        return None, None 

    max_valor = max(lista)
    min_valor = min(lista)
    return max_valor, min_valor

mi_lista = [3, 5, 9, 0, 3, 4]
max_numero, min_numero = encontrar_max_min(mi_lista)
if max_numero is not None and min_numero is not None:
    print(f"El número más grande es: {max_numero}")
    print(f"El número más pequeño es: {min_numero}")
else:
    print("La lista está vacía.")