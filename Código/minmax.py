import random
from Variables_Globales import *

class arbolMin():
    def __init__(self,profundidad,jugadas):
        self.profundidadDeseada=profundidad
        self.profundidad=0
        self.jugadas=jugadas
        self.id=0
        self.profundidad=0
        self.nodos=[]
        self.iniciarArbol()

    def iniciarArbol(self):
        padre=None
        idN=self.id
        for i in self.jugadas:
            padre=nodo(self,self.id,self.profundidad,padre,i)
            self.nodos.append(padre)
            idN+=1

    def añadirNodo(self,nodo):
        self.nodos.append(nodo)
    
    def devolverJugada(self):
        self.calcularArbol()
        return self.elegido
    
    def calcularArbol(self):
        valor=1000000000
        sucesor=None
        for i in self.nodos:
            i.recorrer()
            if i.valor<valor: 
                valor=i.valor
                sucesor=i.estado

        if sucesor==None: 
            nodo=random.choice(self.nodos)
            self.elegido=nodo.estado
        else:
            self.elegido=sucesor



        
class nodo():
    def __init__(self,arbol,id,profundidad,padre,estado) -> None:
        self.arbol=arbol
        self.id=id
        self.profundidad=profundidad
        self.estado=estado
        self.beta=99999
        self.alfa=-99999
        if profundidad%2==0:
            self.max=True
            self.valor=self.alfa
            self.turn=self.estado['NEXT_STATE']['TURN']
        else:
            self.max  =False
            self.valor=self.beta
            self.turn=(self.estado['NEXT_STATE']['TURN']+1)%2
        self.padre=padre
        self.hijos=[]
        
        
        #self.valor=self.calcularValor()
        #self.crearHijos()
        #if self.profundidad==self.arbol.profundidadDeseada: self.propagacion()
    
    def calcularValor(self):
        propias=int(len(self.estado['NEXT_STATE']['GAMER'][self.turn]))+int(self.estado['NEXT_STATE']['CHIPS'][self.turn])
        enemigas=int(len(self.estado['NEXT_STATE']['GAMER'][(self.turn+1)%2]))+int(self.estado['NEXT_STATE']['CHIPS'][(self.turn+1)%2])
        if enemigas<3: return 15
        else: return propias-enemigas

    def __str__(self) -> str:
        return str(self.valor)

    def recorrer(self):
        if self.profundidad!=self.arbol.profundidadDeseada:
            sucesores=generarSucesores(self.estado)
            if len(sucesores)!=0:
                for i in sucesores:
                    self.arbol.id+=1
                    hijo=nodo(self.arbol,self.arbol.id,self.profundidad+1,self,i)
                    hijo.alfa=self.alfa
                    hijo.beta=self.beta
                    hijo.recorrer()
                    if self.max and self.alfa<hijo.valor:
                        self.alfa=hijo.valor
                    elif not self.max and self.beta>hijo.valor:
                        self.beta=hijo.valor    

                    self.hijos.append(hijo)


                    if self.max: self.valor=self.alfa
                    else: self.valor=self.beta

                    if self.alfa>=self.beta:
                        return 
        else:
            self.valor=self.calcularValor()
             
         


    

