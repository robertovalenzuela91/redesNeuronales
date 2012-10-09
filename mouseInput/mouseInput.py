#! /usr/bin/python

import time
from backpropagation import Red_neuronal

class Mouse_listening:
    
    def __init__(self):
        self.mouse = file('/dev/input/mouse1')

    def bits(self, bin, n):
        temp = ""
        bin = bin[2:]
        for i in range(n-len(bin)):
            temp += "0"
        return (temp+bin)

    def listening(self):
        temp = [0]*5

        estado, x, y = tuple(ord(c) for c in self.mouse.read(3))
        estado = self.bits(bin(estado), 8)
        temp[0] = int(estado[7])
        temp[1] = int(estado[6])
        temp[2] = int(estado[5])

        # Movimiento del mouse
        if estado[3] == "1": # Si es 1 el raton se mueve a la izquierda
            x = (256-x)*-1
        if estado[2] == "1": # Si es 1 el raton se mueve hacia abajo
            y = (256-y)*-1

        temp[3] = float(x)
        temp[4] = float(y)

        return temp

def main():
    mouse = Mouse_listening()
    # Entradas, salidas, capas ocultas, neurona por capa,
    n = Red_neuronal(5, 5, 1, 2, 0.95, 0.25 )

    tiempo_min = 0.1
    while True:

        estado = mouse.listening()

        if estado[0] == 1 or estado[1] == 1 or estado[2] == 1:
            print "Lanzar neurona \n Entrada:", estado, "\n Valor de la neurona:", n.evaluar(estado)
        
        bandera = time.time()
        contador = 1
        if estado[3] != 0.0 or estado[4] != 0.0 :
            while (time.time() - bandera) < tiempo_min :

                temp = mouse.listening()

                if temp[0] == 1:
                    estado[0] = 1
                    break
                if temp[1] == 1:
                    estado[1] = 1
                    break
                if temp[2] == 1:
                    estado[2] = 1
                    break

                estado[3] += temp[3]
                estado[4] += temp[4]
                contador += 1

            estado[3] /= contador*256
            estado[4] /= contador*256
 
            print "Lanzar neurona \n Entrada:", estado, "\n Valor de la neurona:", n.evaluar(estado)

main()
