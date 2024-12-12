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
    
    def queue(self,  dato):
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

    def desqueue(self):
        if self.size!=0:
            self.inicio = self.inicio.siguiente
            self.size -= 1
            
            
class persona:

    def __init__(self, nopersona, minutollegada):
        self.nopersona = nopersona
        self.minutollegada = minutollegada
idcliente = 1
contadorminutos = 0
contadorllegada =0
contadorservicio = 0 
contadorclientesatendidos = 0
colacajero = cola()
while contadorminutos < 600:
    if contadorllegada == 0:
        contadorllegada = random.randint(2,3)
        cliente = persona(idcliente,contadorminutos)
        idcliente += 1
        colacajero.queue(cliente)

    if contadorservicio ==0:
        contadorservicio = random.randint(2,4)
        colacajero.desqueue()
        contadorclientesatendidos +=1

    contadorllegada -=1
    contadorservicio -=1
    contadorminutos +=1

print(f"Se atendieron {contadorclientesatendidos} clientes en 10 horas")
print(f"Despues de 10 horas hay {colacajero.size} clientes en cola")
print(f"La persona que quedo en frente de la cola despues de las 10 horas llego a los {colacajero.inicio.dato.minutollegada} minutos")