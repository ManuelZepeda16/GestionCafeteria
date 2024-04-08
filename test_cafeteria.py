import pytest
from cafeteria import validFormat

# El programa ignora los espacios en blanco de la entrada

@pytest.mark.parametrize("array, expected", [
    ("C, 1, 2, 3, 4, 5", False), # Nombre con menos de 2 caracteres
    ("Cofeeeeeeeeeeeeeeeeeeeeeeeee, 1, 2, 3, 4, 5", False), # Nombre con mas de 15 caracteres
    ("C0ff33, 1, 2, 3, 4, 5", False), # Nombre con caracteres no alfabéticos
    ("Coffee, 1, 2, 3, 4, 5", True), # Nombre dentro del rango
    ("Coffee, 1, 2, 3, 4, 5, 6", False), # Bebida con más de 6 tamaños
    ("Coffee, 48", True), # Bebida con al menos un tamaño
    ("Coffee, 1 , 2, 3", True),  # Número de tamaños dentro del rango
    ("Coffee", False), # Solo el nombre de la bebida
    ("Coffee, 11, 12, 13, 45, 49", False), # Tamaño mayor a 48
    ("Coffee, 0, 12, 13, 15, 45", False), # Tamaño menor a 1
    ("Coffee, 1, 45, 46, 47, 48", True), # Tamaños dentro del límite
    ("Coffee, 1, 2, 3, 5, 4", False), # Los tamaños no son ascendentes
    ("Coffee, 7, 8, 9, 10, 11", True), # Los tamaños son ascendentes
    ("Coffee, 7, 8, 9, 11, 11", False), # Tamaño repetido (no ascendente)
    ("Coffee, 7, 8, 9, -10, 11", False), # El tamaño no es un número entero
    ("12, Coffee, 13, 14, 15", False), # El nombre no es el primer parámeto
    ("Coffee, 1, 2", True), # Nombre en en la primera posición
    ("Coffee,, 1, 2, 3, 4, 5", False), # La entrada este separada por más de una coma
    ("   Coffee ,15,   19 ,    20  ,    23", True), # La entrada contiene espacios en blanco
])

def test_validFormat(array, expected):
    assert validFormat(array) == expected
