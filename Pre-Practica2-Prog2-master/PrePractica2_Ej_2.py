#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
listaoriginal=[]
x= (int(input("Ingrese la longitud de la lista: ")))
for i in range(x):
    y = input("Ingrese numero: ")
    listaoriginal.append(int(y))
print(listaoriginal)

listaimpar=[]
for i in listaoriginal:
    if (i%2) != 0:
        listaimpar.append(int(i))
print(listaimpar)


#FIN