
numeros = []


while True:
    entrada = input("Ingrese un número (o presione Enter para finalizar): ")
    if entrada == "":
        break  
    try:
        numero = float(entrada)  
        numeros.append(numero) 
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

numeros.sort()
print("Números ordenados de menor a mayor:", numeros)