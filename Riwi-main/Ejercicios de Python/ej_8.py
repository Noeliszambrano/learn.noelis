
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operador = input("Ingresa un operador (+, -, *, /): ")


if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 == 0:
        resultado = "Error: División por cero"
    else:
        resultado = num1 / num2
else:
    resultado = "Operador inválido"

# Imprime el resultado
print("El resultado es:", resultado)