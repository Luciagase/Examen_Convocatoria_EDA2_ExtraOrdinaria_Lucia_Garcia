import pytest
from armaduras import Armadura

def test_calificacion_armaduras():
    # Crear una lista con objetos Armadura
    armaduras = [
        Armadura("Mark-42", "3-7"),
        Armadura("Mark-50", "5-2"),
        Armadura("Mark-7", "1-9"),
    ]

    # Recorrer los elementos de la lista y ejecutar el método calificacion en cada objeto
    for armadura in armaduras:
        armadura.calificacion()

# Ejecutar el test
pytest.main()
