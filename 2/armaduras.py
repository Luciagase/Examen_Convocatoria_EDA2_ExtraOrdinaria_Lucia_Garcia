
class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Armadura:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        

    def __str__(self):
        return "Armadura creada con éxito"

    def __repr__(self):
        return f"Nombre ({self.name},  Rango: {self.tipo})"

    def calificacion(self):
        codigo_legion = self.nombre[:3]
        identificacion_coherente = len(self.nombre) % 2 == 0
        identificacion_siglo = self.nombre[0].isdigit()
        numero_armadura = int(self.rango.split('-')[1])
        numero_escuadra = int(self.rango.split('-')[0])

        print("Clasificación de la armadura:")
        print("Código de legión:", codigo_legion)
        print("Identificación coherente:", identificacion_coherente)
        print("Identificación de siglo:", identificacion_siglo)
        print("Número de armadura:", numero_armadura)
        print("Número de escuadra:", numero_escuadra)

class Lista:
    def __init__(self):
        self.head = None
    
    def insertar(self, armadura):
        new_node = Nodo(armadura)
        if self.head is None:
            self.head = new_node
        elif self.head.data.rango < armadura.rango:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data.rango > armadura.rango:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def mostrar(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

