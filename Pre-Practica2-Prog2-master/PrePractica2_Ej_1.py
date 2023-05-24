#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
lista=[]
print("Lista")
x=int(input("Ingrese la longitud de la lista: "))
for i in range(x):
    y = input("Ingrese numero: ")
    lista.append(int(y))

print(f"El numero mayor es {max(lista)}")

numeromayor=lista[0]
for i in range(1, x):
    if lista[i] > numeromayor:
        numeromayor=lista[i]
print(f"El numero mayor es {numeromayor}")
""""FINALIZAR"""

#FIN