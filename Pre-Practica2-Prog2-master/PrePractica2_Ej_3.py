#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
x= int(input("Ingrese un numero: "))
y= int(input("Ingrese otro numero: "))

try:
    z = x/y
except ZeroDivisionError as exepction:
    print(f"Ocurrio un error | {exepction}")
else:
    print(f"El resultado de la division da {z}")

#FIN