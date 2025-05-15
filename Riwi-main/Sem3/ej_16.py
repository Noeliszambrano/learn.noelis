import re

def validar_contrasena(contrasena):

  if len(contrasena) < 8:
    return False

  if not re.search(r"[A-Z]", contrasena):
    return False

  if not re.search(r"[a-z]", contrasena):
    return False

  if not re.search(r"[0-9]", contrasena):
    return False

  if not re.search(r"[^a-zA-Z0-9]", contrasena):
    return False

  return True
contrasena_valida = "Contraseña123!"
contrasena_invalida = "contraseña123"  
print(f"'{contrasena_valida}' es válida: {validar_contrasena(contrasena_valida)}")
print(f"'{contrasena_invalida}' es válida: {validar_contrasena(contrasena_invalida)}")