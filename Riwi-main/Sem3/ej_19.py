import random
import string

def generar_contrasena_aleatoria(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena
longitud_deseada = 12
contrasena_generada = generar_contrasena_aleatoria(longitud_deseada)
print(f"La contraseña generada es: {contrasena_generada}")