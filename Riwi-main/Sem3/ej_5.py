def celsius_a_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

try:
  temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
except ValueError:
  print("Entrada inválida. Por favor, ingrese un número.")
  exit()
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"La temperatura {temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")