"""Sum, Compresión de Listas, Map, Filter, Reduce."""

from typing import Iterable

###############################################################################


numeros = [1, 2, 3, 4, 5, 6]


"""
Escribir una función lambda que eleve los elementos al cubo

Restricción: Utilizar List, map y lambda y la variable numeros
"""

numeros_al_cubo =  list(map(lambda x: x ** 3, numeros))
print (numeros_al_cubo)

"""
Escribir una función lambda que permita filtrar todos los elementos pares

Restricción: Utilizar List, filter, lambda y la variable numeros_al_cubo
"""

numeros_al_cubo_pares =  list(filter(lambda x: x%2 == 0,numeros_al_cubo))


"""
Escribir una función Lambda que sume todos los elementos

Restricción: Utilizar reduce, lambda y la variable numeros_al_cubo_pares
"""

from functools import reduce  # noqa: E402

suma_numeros_al_cubo_pares =  reduce(lambda x,y: x+y,numeros_al_cubo_pares)


# NO MODIFICAR - INICIO
assert numeros_al_cubo == [1, 8, 27, 64, 125, 216]
assert numeros_al_cubo_pares == [8, 64, 216]
assert suma_numeros_al_cubo_pares == 288
# NO MODIFICAR - FIN
