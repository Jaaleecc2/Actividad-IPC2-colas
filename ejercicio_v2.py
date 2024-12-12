import random
class node:
    def __init__(self, dato, siguiente=None, anterior=None) -> None:
        
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

class cola:
    def __init__(self, inicio =None, size=0)-> None:
        self.inicio = inicio
        self.size = size 
    
    def enqueue(self,  dato):
        newdato = node(dato)
        if self.size==0:
            self.inicio = newdato
            self.size +=1
        else:
            aux = self.inicio
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = newdato
            self.size = self.size +1

    def dequeue(self):
        if self.size!=0:
            self.inicio = self.inicio.siguiente
            self.size -= 1
            
            
class persona:
    def __init__(self, nopersona, minutollegada):
        self.nopersona = nopersona
        self.minutollegada = minutollegada

#funciones
def agregar_cliente():

#variables globales
cola_cajero = cola()
contador_minutos = 0

#variables llegada
no_clientes_entrando = 0

#variables salida
no_clientes_salida = 0

