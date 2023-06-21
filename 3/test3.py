import pytest
from ej3 import Armadura

def test_str_armaduras():
    # Crear una lista con objetos Armadura
    armaduras = [
        Armadura("Mark-42", "3-7"),
        Armadura("Mark-50", "5-2"),
        Armadura("Mark-7", "1-9"),
    ]

    # Recorrer los elementos de la lista y utilizar print para mostrar la información del str
    for armadura in armaduras:
        print(armadura)

# Ejecutar el test
pytest.main()
