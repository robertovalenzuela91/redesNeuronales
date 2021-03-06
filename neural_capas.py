from numpy import array
from sys import argv
import random

ACTIVACION = 1.0
DESACTIVACION = -1.0
TASA_DE_APRENDIZAJE = 0.05

class Condicion:
    def __init__(self, dim):
        #Vector de pesos de la neurona
        self.w = self.pesos(dim)
    #Genera de manera al azar un vector de pesos dado el tamanio
    # del vector de entrada
    def pesos(self, w):
        global ACTIVACION, DESACTIVACION
        lista = list()
        for i in range(w + 1):
            lista.append(random.uniform(DESACTIVACION, ACTIVACION))
        lista = array(lista)
        return lista
    def calcula(self, entrada):
        global ACTIVACION, DESACTIVACION
        self.x = entrada
        self.a = sum(self.x * self.w)
        if self.a >= 0.0:
            self.y = ACTIVACION
        else:
            self.y = DESACTIVACION
        return self.y

class Neurona(Condicion):
    def __init__(self, dim):
        Condicion.__init__(self, dim)
        return
    #Calcula el producto de vector de entrada por vector de pesos
    #nos da una activacion o desactivacion

    def entrena(self, entrada, respuestaDeseada):
        global TASA_DE_APRENDIZAJE
        self.calcula(entrada)
        self.respuesta = respuestaDeseada
        self.cambio = TASA_DE_APRENDIZAJE * (self.respuesta - self.y) * self.x
        self.w += self.cambio
        return

#Genera dummies que son nuestro vector de entrada a la neurona
# de una n dimension dada de manera uniformemente
#aleatoria dentro del rando de activacion y desactivacion

def genera(dimension):
    global ACTIVACION, DESACTIVACION
    lista = list()
    for i in range(dimension):
        value = random.uniform(DESACTIVACION, ACTIVACION)
        lista.append(value)
    lista.append(-1.0)
    x = array(lista)
    return x
        
#Se le da a la neurona una n dimension para que genere
# su vector de pesos, para luego se generen una cierta cantidad
# de vectores que la neurona va ir clasificando

class Capa:
    def __init__(self, tamanio, dim):
        self.capa = self.inicializaNeurona(tamanio, dim)
        self.tamanio = tamanio
        
    def inicializaNeurona(self, tamanio, dim):
        capa = list()
        for e in range(tamanio):
            capa.append([Neurona(dim),Condicion(dim)]) 
        return capa

    def calculaCondicion(self, entrada):
        self.entrada = entrada
        for e in range(len(self.capa)):
            respuestaDeseada = self.capa[e][1].calcula(entrada)
            self.capa[e][0].entrena(entrada, respuestaDeseada)



def main():
    try:
        dim = int(argv[1])
    except:
        dim = 2
    tamanio_de_capa = 20
    capa = Capa(tamanio_de_capa, dim)
    print "Vector de pesos inicial de las neuronas"
    for e in range(tamanio_de_capa):
        for i in range(2):
            print capa.capa[e][i].w
    print "########################################"
    for i in range(5000):
        entrada = genera(dim)
        capa.calculaCondicion(entrada)
    print "Vector de pesos inicial de las neuronas"
    for e in range(tamanio_de_capa):
        for i in range(2):
            print capa.capa[e][i].w
    print "########################################"
main()
