contactos = {}

print("Bienvenido a Riwi inventario")
while True:
    print("[1] para ingresar contacto")
    print("[2] para consultar contacto")
    print("[3] para actualizar datos de contacto")
    print("[4] para eliminar contacto")
    print("[6] Salir")
    menu = input("Digite una opcion: ")
    if menu == "1":
        nombre = input("Digite nombre del contacto: ")
        if nombre in contactos:
             print("Este nombre ya se encuentra en contactos")
        else:
             numero = input("Digite el numero: ")
             email = input("Digite el email: ")
             contactos[nombre] = {"numero": numero, "email": email}
    elif menu == "2":
        nombre = input("Digite nombre del contacto a buscar: ")
        if nombre in contactos:
             email = contactos[nombre]["email"]
             numero = contactos[nombre]["numero"]
             print(f"Nombre: {nombre}")
             print(f"Numero: {numero}")
             print(f"Email: {email}")
        else:
             print("Este nombre no se encuentra en contactos")
    elif menu == "3":
        nombre = input("Digite nombre del contacto a modificar: ")
        if nombre in contactos:
             numero = input("Digite el numero: ")
             email = input("Digite el email: ")
             contactos[nombre]["email"] = email
             contactos[nombre]["numero"] = numero
        else:
             print("Este nombre no se encuentra en contactos")
    elif menu == "4":
        nombre = input("Digite nombre del contacto a modificar: ")
        if nombre in contactos:
            contactos.pop(nombre)
        else:
            print("Este nombre no se encuentra en contactos")
    elif menu == "5":
        break     
    else:
        print("El valor es invalido")
    continuar = input("Desea regresar al menu? (n/s)")
    if continuar == "n":
         break