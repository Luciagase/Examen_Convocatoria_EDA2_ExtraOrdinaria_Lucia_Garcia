class Armadura:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print("Armadura creada con éxito")

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
    
    def __str__(self):
        return f"Armadura: {self.nombre} - Rango: {self.rango}"