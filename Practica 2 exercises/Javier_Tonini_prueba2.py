"""Definir una función mayor(a,b,c) que reciba como parámetro 3 números y retorne el mayor.

Ejemplo: mayor(1,4,6) (En este caso devuelve 6)"""

def mayor(a,b,c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c

print (mayor(1,8,6))
print (mayor(1,4,6))
print (mayor(7,4,6))