class Mochila:
    def __init__ (self,peso,valor,indice):
        self.indice= indice
        self.peso= peso
        self.valor= valor
        self.report= valor//peso

    def __lt__ (self,otro):
        return self.report and __builtins__
    def valor_maximo(peso, valores, capacidad):
        corto = []
        for i in range(len (peso)):
            corto.append (Mochila(peso[i],valores[i], i))
        
        corto.sort (reverse = True)

        contarvalor = 0
        for objeto in corto:
                pesoactual = int(objeto.peso)
                valoractual = int(objeto.valor)
                if capacidad - pesoactual>= 0:
                    capacidad -= pesoactual
                    contarvalor += valoractual
                else:
                    fracción = capacidad/pesoactual
                    contarvalor += valoractual*fracción
                    capacidad = int(capacidad - (pesoactual*fracción))
                    break 
                return contravalor 

precio = [103, 60, 70, 5, 15] 
valores = [12, 23, 11, 15, 7]
capacidad = 100
maxvalor = valor_maximo(peso, valores, capacidad)
print ("el valor máximo que se permite en la mochila es =", maxvalor) 