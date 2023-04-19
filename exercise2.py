"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

esta_lloviendo = True
riego_activado = True

# COMPLETAR - INICIO
piso_mojado = esta_lloviendo or riego_activado #Puede ser asi
piso_mojado = True
if esta_lloviendo == True or riego_activado == True:
    piso_mojado = True
    print(piso_mojado)
else:
    piso_mojado = False
# COMPLETAR - FIN

assert piso_mojado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

# COMPLETAR - INICIO
area_mayor_a_cinco = True

if not(area_cuadrado < 5):
    print(area_mayor_a_cinco)
else:
    print(area_mayor_a_cinco = False)

# COMPLETAR - FIN

assert area_mayor_a_cinco


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50

# COMPLETAR - INICIO
resultado = True
if numero_1%7 == 0 and numero_2%7 != 0:
    print(resultado)
else:
    print(not(resultado))
# COMPLETAR - FIN

assert resultado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100

# COMPLETAR - INICIO
if variable_01== 80 or variable_02== 80 or variable_03== 80 or variable_04== 80 or variable_05== 80:
    resultado = variable_03
    print(resultado)
# COMPLETAR - FIN

assert resultado == 80