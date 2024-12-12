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

#CREACIÓN DE VARIABLES INICIALES
no_persona = 1
contador_minutos = 0
colaCajero= cola()
contador_minutos_extra = 0

#INGRESO DEL PRIMER CLIENTE
min_primer_cliente =random.randint(2, 3)
primer_cliente = persona(no_persona, min_primer_cliente)
colaCajero.enqueue(primer_cliente)
no_persona += 1
contador_minutos += min_primer_cliente
contador_deben = 0

while contador_minutos < 600:
    minuto_llegada = random.randint(2, 3)
    minuto_salida = random.randint(2, 4)

    if(contador_minutos_extra >= minuto_llegada):
        cliente = persona(no_persona, minuto_llegada)
        colaCajero.enqueue(cliente)
        no_persona +=1
        contador_minutos_extra -= minuto_llegada
    
    elif((contador_minutos_extra < 0) and (abs(contador_minutos_extra) >= minuto_salida)):
        colaCajero.dequeue()
        contador_minutos_extra +=minuto_salida

    elif(minuto_llegada < minuto_salida):
        contador_minutos += minuto_llegada
        cliente = persona(no_persona, contador_minutos)
        no_persona +=1
        colaCajero.enqueue(cliente)

        if(contador_minutos >= 600):
            break
        
        diferencia_salida_llegada = minuto_salida - minuto_llegada
        contador_minutos_extra += diferencia_salida_llegada
        contador_minutos += diferencia_salida_llegada
        colaCajero.dequeue()
    elif(minuto_salida < minuto_llegada):
        contador_minutos += minuto_salida
        colaCajero.dequeue()

        if(contador_minutos >=600):
            break

        diferencia_llegada_salida = minuto_llegada - minuto_salida
        contador_minutos += diferencia_llegada_salida
        contador_minutos_extra -= diferencia_llegada_salida
        cliente = persona(no_persona, contador_minutos)
        colaCajero.enqueue(cliente)
        no_persona +=1
    
    elif(minuto_salida == minuto_llegada):
        contador_minutos += minuto_llegada
        if(contador_minutos > 600):
            break
        else:
            cliente = persona(no_persona, contador_minutos)
            colaCajero.enqueue(cliente)
            no_persona +=1
            colaCajero.dequeue()

print("\nCantidad de clientes atendidos: " + str(no_persona - 1))
print("Cantidad de clientes después de las 10 horas: "+ str(colaCajero.size))
print("Tiempo de primer cliente no atendido: " + str(colaCajero.inicio.dato.minutollegada) + " minutos.")
#print(contador_minutos)