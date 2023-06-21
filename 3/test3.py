import random
import unittest

from ej3 import Armadura

class TestArmadura(unittest.TestCase):
    def setUp(self):
        self.Azul = Armadura("Mark-42", "3-7")
        self.Rosa = Armadura("Mark-50", "5-2")
        self.Granate = Armadura("Mark-7", "1-9")


    def test_calificacion(self):
        self.Azul.calificacion("Mark-42")
        self.assertEqual(self.Azul.calificacion("Mark-42"))
        
