"""Expresiones Booleanas."""


def es_vocal_if(letra: str) -> bool:
    y = str.lower(letra)
    if "a"==y:
        x = True
        return x
    if "e"==y:
        x = True
        return x
    if "i"==y:
        x = True
        return x
    if "o"==y:
        x = True
        return x
    if "u"==y:
        x = True
        return x
    x = False
    return x
    """Toma un string y devuelve un booleano en base a si letra es una vocal o
    no.

    Restricciónes:
        - Utilizar un if para cada posibilidad.
        - Utilizar la función lower() sólo una vez.
        - No utilizar ELSE.
        - Utilizar 6 returns.

    Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
    """


# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
assert es_vocal_if("e")
assert es_vocal_if("E")
# NO MODIFICAR - FIN


###############################################################################



def es_vocal_if_in(letra: str) -> bool:
    y = str.lower(letra)
    tupla = ("a","e","i","o","u")
    if y in tupla:
        x = True
        return x
    x = False
    return x
    
    """Re-escribir utilizando un sólo IF y el operador IN.

    Restricciónes:
        - Utilizar un único IF.
        - Utilizar dos returns.
        - No utilizar ELSE.
        - No utilizar FOR.
        - No utilizar listas.

    Referencia: https://docs.python.org/3/reference/expressions.html#membership-test-operations # noqa: E501
    """
    


# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    """Re-escribir como expresión booleana utilizando el operador IN

    Restricciónes:
        - No utilizar IF.
        - Utilizar un único return.
        - No utilizar FOR.
        - No utilizar listas.
    """
    y = str.lower(letra)
    tupla = ("a","e","i","o","u")
    return y in tupla

# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
