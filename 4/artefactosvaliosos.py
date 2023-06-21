import unittest

class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Artefactos_valiosos:
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad

    def __str__(self):
        return f"El artefacto {self.nombre} pesa {self.peso} gramos y cuesta {self.precio}"
    
class ListaArtefacto:
     
    def __init__(self):
        self.head = None
    
    def insertar(self, artefacto):
        new_node = Nodo(artefacto)
        if self.head is None:
            self.head = new_node
        elif self.head.data.fecha_caducidad > artefacto.fecha_caducidad:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data.fecha_caducidad < artefacto.fecha_caducidad:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def mostrar(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def modificar(self, artefacto, caracteristica, valor):
        current = self.head
        while current and current.data.nombre != artefacto.nombre:
            current = current.next
        if current:
            if caracteristica == "peso":
                current.data.peso = valor
            elif caracteristica == "nombre":
                current.data.nombre = valor
            elif caracteristica == "precio":
                current.data.precio = valor
            elif caracteristica == "fecha_caducidad":
                current.data.fecha_caducidad = valor
            else:
                print("Caracteristica no encontrada")
        else:
            print("artefacto no encontrado")


        


class TestArtefacto(unittest.TestCase):
    def setUp(self):
        # Crear un numero arbitrario
        self.artefacto1 = Artefactos_valiosos(100, "artefacto1", 1000, "01/01/2020")
        self.artefacto2 = Artefactos_valiosos(200, "artefacto2", 2000, "02/02/2020")
        self.artefacto3 = Artefactos_valiosos(300, "artefacto3", 3000, "03/03/2020")

    def test_artefacto(self):
        self.assertEqual(self.artefacto1.peso, 100)
        self.assertEqual(self.artefacto1.nombre, "artefacto1")
        self.assertEqual(self.artefacto1.precio, 1000)
        self.assertEqual(self.artefacto1.fecha_fabricacion, "01/01/2020")
        self.assertEqual(self.artefacto2.peso, 200)
        self.assertEqual(self.artefacto2.nombre, "artefacto2")
        self.assertEqual(self.artefacto2.precio, 2000)
        self.assertEqual(self.artefacto2.fecha_fabricacion, "02/02/2020")
        self.assertEqual(self.artefacto3.peso, 300)
        self.assertEqual(self.artefacto3.nombre, "artefacto3")
        self.assertEqual(self.artefacto3.precio, 3000)
        self.assertEqual(self.artefacto3.fecha_fabricacion, "03/03/2020")
    
    # comprobar que el metodo __str__ funciona correctamente
    def test_str(self):
        self.assertEqual(str(self.artefacto1), "El artefacto1 pesa 100 gramos y cuesta 1000")
        self.assertEqual(str(self.artefacto2), "El artefacto2 pesa 200 gramos y cuesta 2000")
        self.assertEqual(str(self.artefacto3), "El artefacto3 pesa 300 gramos y cuesta 3000")

    def test_insertar_mostrar(self):
        lista_artefacto = ListaArtefacto()
        lista_artefacto.insertar(self.artefacto1)
        lista_artefacto.insertar(self.artefacto2)
        lista_artefacto.insertar(self.artefacto3)
        lista_artefacto.mostrar()
        assert lista_artefacto.head.data.nombre == "artefacto1"
        assert lista_artefacto.head.next.data.nombre == "artefacto2"
        assert lista_artefacto.head.next.next.data.nombre == "artefacto3"


    def test_modificar(self):
        
        lista_artefacto = ListaArtefacto()
        lista_artefacto.insertar(self.artefacto1)
        lista_artefacto.insertar(self.artefacto2)
        lista_artefacto.insertar(self.artefacto3)
        lista_artefacto.modificar(self.artefacto1, "precio", 5000)
        
        assert lista_artefacto.head.data.precio == 5000



if __name__ == "__main__":
    unittest.main()