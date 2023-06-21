#sable
import random 

class ArtefactosValiosos():
    peso = 0
    nombre = ""
    precio = 0
    fecha_caducidad = "00/00/0000"

    def _init_(self,peso,nombre,precio,fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        print('La conserva se ha creado con éxito')
    
    def _str_(self):
        return f"PESO:\t{self.peso}\n" \
            f"NOMBRE:\t{self.nombre}\n" \
            f"PRECIO:\t{self.precio}\n" \
            f"FECHA DE CADUCIDAD:\t{self.fecha_caducidad}\n"

    def menor(artefacto1,artefacto2):
        return (int(artefacto1.fecha_caducidad[6:10]) < int(artefacto2.fecha_caducidad[6:10]) or (int(artefacto1.fecha_caducidad[6:10]) == int(artefacto2.fecha_caducidad[6:10])
            and int(artefacto1.fecha_caducidad[3:5]) < int(artefacto2.fecha_caducidad[3:5])) or (int(artefacto1.fecha_caducidad[6:10]) == int(artefacto2.fecha_caducidad[6:10])
            and int(artefacto1.fecha_caducidad[3:5]) == int(artefacto2.fecha_caducidad[3:5]) and int(artefacto1.fecha_caducidad[0:2]) < int(artefacto2.fecha_caducidad[0:2])))

    def quicksort(lista,primero,ultimo):
        izq = primero
        der = ultimo-1
        pivote = ultimo
        while (izq < der):
            while (artefactosvaliosos.menor(lista[izq],lista[pivote]) and izq <= der):
                izq += 1
            while (artefactosvaliosos.menor(lista[pivote],lista[der]) and izq <= der):
                der-=1
            if (izq < der):
                lista[izq],lista[der] = lista[der],lista[izq]
        if (artefactosvaliosos.menor(lista[pivote],lista[izq])):
            lista[izq],lista[pivote] = lista[pivote],lista[izq]
        if (primero < izq):
            artefactosvaliosos.quicksort(lista,primero,izq-1)
        if (ultimo > izq):
            artefactosvaliosos.quicksort(lista,izq+1,ultimo)

if __name__ == "_main_":
    lista = [artefactosvaliosos(10,"LIBRO",20,"02/10/2034"),
                artefactosvaliosos(5,"ZANAHORIAS",8,"24/03/2023"),
                artefactosvaliosos(30,"ORDENADOR",1200,"14/09/2028"),
                artefactosvaliosos(50,"JAMÓN",140,"14/05/2024")]
        
   def hijo_sin_amor(mochila,idx):
        if (idx < len(mochila)):
            if (mochila[idx].nombre == "ANILLO DE PODER"):
                return True, idx
            else:
                return hijo_sin_amor(mochila,idx+1)
        else:
            print("La mochila no contiene un anillo de poder")
            return False, -1