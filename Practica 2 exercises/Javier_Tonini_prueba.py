"""Crear una función que:

Tome como parámetro una lista de números y devuelva el producto todos los números.
Si la lista está vacía debe devolver 0.
Ejecutar dicha función para verificar su correcto funcionamiento."""

def producto(lista):
    producto = 1
    for x in lista:
        producto *= x
    return producto

a=[1,2,3,4,5]
b=[1,2,3,4,5,0]
print("El producto de la lista a es: ", producto(a))
print("El producto de la lista b es: ", producto(b))