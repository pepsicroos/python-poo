from particula import Particula
import json
from grafo import Grafo
from nodo import Nodo
from arista import *



class AdministraParticulas:
    def __init__(self):
        self.__particulas=[]
        self.grafo = Grafo()
        



    def agregaInicio(self, Particula):
        self.__particulas.insert(0, Particula)

    def agregaFinal(self, Particula):
        self.__particulas.append(Particula)

    def mostrar(self):
        for Particula in self.__particulas:
            print(Particula)
    
            
    def __str__(self):
        return "".join(
            str(Particula) +'\n' for Particula in self.__particulas
        )

    
    def guardar(self, ubicacion):

        try:
            with open(ubicacion, 'w') as archivo:

                lista=[Particula.to_dict() for Particula in self.__particulas]
                print(lista)
                json.dump(lista,archivo, indent=5)
            return 1
        
        except:
            return 0

    

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as newarchivo:
                lista=json.load(newarchivo)
                
                self.__particulas=[Particula(**particula) for particula in lista]
                
            return 1
        
        except:
            return 0

    
    

    def __len__(self):
        return len(self.__particulas)

    
    def __iter__(self):
        self.count = 0
        return self

    
    def __next__(self):
        if self.count < len(self.__particulas):
            par = self.__particulas[self.count]
            self.count += 1
            return par
        else:
            raise StopIteration



    def ordenapor_ID(self):
        self.__particulas.sort(key=lambda Particula:Particula.Id)




    def ordenaporVelocidad(self):
        self.__particulas.sort(key=lambda Particula:Particula.Velocidad)
        



    def ordenaporDistancia(self):
        self.__particulas.sort(key=lambda Particula:Particula.distancia, reverse=True)

    def getpuntos(self) -> list:
        puntos=[]

        for part in self.__particulas:
            ox=part.Origen_x
            oy=part.Origen_y
            dx=part.Destino_x
            dy=part.Destino_y

            punto=(ox,oy,dx,dy)
            puntos.append(punto)
        
        return puntos
    

    def metodo_dijkstra(self, origen: Nodo):
        nodo = Nodo(origen)
        dijkstra = self.grafo.dijkstra(nodo)
        return dijkstra
    
    def mostrarDijkstra(self, grafo:dict):
        for nodo, value in grafo.items():
            print(nodo, ":", value)


        
        

        
       
        
        
        

    
           

        
            
            
            
           
            
        
        
            
            
                



"""lista1=Particula("asdasd",10,10,10,10,100,10,10,19)
lista2=Particula("asdasd",10,10,10,10,150,10,10,19)
lista3=Particula("asdasd",10,10,10,10,200,10,10,19)
prueba=AdministraParticulas()
prueba.agregaInicio(lista1)
prueba.agregaInicio(lista2)
prueba.agregaInicio(lista3)
print(prueba.ordenaporVelocidad())
print("Separa \n")
print(prueba)"""
    


    


