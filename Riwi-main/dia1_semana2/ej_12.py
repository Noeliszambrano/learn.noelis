Lista=["Naranja", "Pera", "Manzana","Sandia","Mango"]

print("Lista de frutas:", Lista)

eliminar=input("Ingrese la fruta que desea eliminarinar ")

if eliminar in Lista:
    Lista.remove(eliminar)
    print(Lista)
