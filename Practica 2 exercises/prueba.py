def lista_palabras(lista):
    listanumeros =[]
    for x in lista:
        listanumeros.append(len(x))
    return listanumeros

lista = ["hola","adios","buenas"]
print (lista_palabras(lista))
