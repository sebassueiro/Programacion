"""DataClasses y Sobrecarga de operadores."""

from dataclasses import dataclass
from typing import List


"""Una carrera tiene varias materias, la "longitud" de una carrera hace
referencia a cuantas materias tiene.

Cada materia tiene un nombre.

Escribir una estructura de clases que refleje lo anterior.

Restricciones:
    - Utilizar Dataclasses
    - Utilizar 2 clases
    - Utilizar 1 variables de instancia en cada clase
    - Utilizar 1 método mágico
    - No utilizar variables de clase
    - No utilizar métodos de clase
    - No utilizar métodos de instancia
    - No utilizar properties
    - Utilizar Type Hints en todos los métodos y variables"""

@dataclass
class Materia:
    nombre: str

@dataclass
class Carrera:
    longitud:list
    def __str__(self):
        print(self.longitud)
        return f"Carrera(materias={self.longitud})"
    


# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    materia = Materia()
    assert False, "No se puede instanciar sin nombre"
except TypeError:
    assert True

try:
    materia = Carrera()
    assert False, "No se puede instanciar sin materias"
except TypeError:
    assert True

# Test básico
matematica = Materia("Matematica")
assert matematica.nombre == "Matematica"

estadistica = Materia(nombre="Estadistica")
assert estadistica.nombre == "Estadistica"

ciclo_basico = Carrera([matematica, estadistica])
assert (
    str(ciclo_basico)
    == "Carrera(materias=[Materia(nombre='Matematica'), Materia(nombre='Estadistica')])"  # noqa: 501
)

assert len(ciclo_basico.longitud) == 2
# NO MODIFICAR - FIN
