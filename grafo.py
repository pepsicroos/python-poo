from arista import *
from nodo import *
from collections import deque
from queue import PriorityQueue


class Grafo:
    def __init__(self) -> None:
        self.__aristas=[]
        self.__ady={}
        
    
    def agrega_arista(self, arista:Arista):
        if arista not in self.__aristas:
            self.__aristas.append(arista)
            
    
    def elimina_arista(self,arista):
        self.__aristas.remove(arista)
        
    def __str__(self) -> str:
        return str([str(arista)for arista in self.__aristas])


    def get_list_ady(self) -> dict:
        self.__ady.clear()
        
        for arista in self.__aristas:
            if arista.dirigido():
                n1=arista.get_nodo1()
                n2=arista.get_nodo2()
                peso=arista.peso
                self.agregar_dict(n1,n2,peso)
            else:
                n1 = arista.get_nodo1()
                n2 = arista.get_nodo2()
                self.agregar_dict(n1,n2, arista.peso)
                self.agregar_dict(n2,n1, arista.peso)


        
        return self.__ady
    
    
                
        
    
    def agregar_dict(self,n1,n2, peso):
        if n1 in self.__ady:
            self.__ady[n1].append([n2, peso])
        else:
            self.__ady[n1]=[[n2,peso]]
            


    def print_ady(self):
        self.get_list_ady()
        for key in self.__ady.keys():
            print(key, "--->", end="")
            for value in self.__ady[key]:
                nodo=value[0]
                peso=value[1]
                print(f"[{nodo}, {peso}]", "," , end="")
            print("\n")
            
    
            
            
    def string_window(self):
        string=""
        self.get_list_ady()
        for key in self.__ady.keys():
            string+=str(key)+" ---> "
            for value in self.__ady[key]:
                nodo=value[0]
                string+=str(nodo)
            string+="\n"
        return string
    
    
    def recorrido_profundidad(self, inicio:Nodo):
        visitados=[]
        pila=deque()
        recorrido=[]
        
        grafo=self.get_list_ady()
        
        if inicio not in grafo:
            return recorrido
        
        pila.append(inicio)
        visitados.append(inicio)
        
        while len(pila)>0:
            nodo=pila.pop()
            recorrido.append(nodo)
            
            for ady in grafo[nodo]:
                if ady[0] not in visitados:
                    pila.append(ady[0])
                    visitados.append(ady[0])
        
        return recorrido    
    
    
    def recorrido_amplitud(self, inicio:Nodo):
        visitados=[]
        pila=deque()
        recorrido=[]
        
        grafo=self.get_list_ady()
        
        if inicio not in grafo:
            return recorrido
        
        pila.append(inicio)
        visitados.append(inicio)
        
        while len(pila)>0:
            nodo=pila.popleft()
            recorrido.append(nodo)
            
            for ady in grafo[nodo]:
                if ady[0] not in visitados:
                    pila.append(ady[0])
                    visitados.append(ady[0])
        
        return recorrido 
    
    
    def get_key(self, val:Nodo):
        self.get_list_ady()
        for key in self.__ady.keys():
            if val==key:
                return True
        return False
    
    
    def algoritmo_prim(self, inicio:Nodo):
        grafo=self.get_list_ady()
        g={}
        visitados=[]
        pq=PriorityQueue()
        arbol=[]
        
        
        visitados.append(inicio)
        for ady in  self.__ady[inicio]:
            pq.put((ady[1], inicio, ady[0]))
            
        while not pq.empty():
            arista=pq.get()
            peso = arista[0]
            origen = arista[1]
            destino = arista[2]

            if destino not in visitados:
                visitados.append(destino)
                for ady in  self.__ady[destino]:
                    if ady[0] not in visitados:
                        pq.put((ady[1], destino, ady[0]))
                arbol.append(arista)
                
                if origen in g:
                    g[origen].append([destino, peso])
                else:
                    g[origen] = [[destino, peso]]

                if destino in g:
                    g[destino].append([origen, peso])
                else:
                    g[destino] = [[origen, peso]]
            

        for key in g.keys():
            print(key, "--->", end="")
            for value in g[key]:
                nodo=value[0]
                peso=value[1]
                print(f"[{nodo}, {peso}]", "," , end="")
            print("\n")
    

        return arbol
    

    def kruskal(self ):
        self.get_list_ady()
        g=[]
        lista=[]
        for key in self.__ady.keys():
            for value in self.__ady[key]:
                nodo=value[0]
                peso=value[1]
                arista=(peso, key, nodo)
                lista.append(arista)
                
        
        lista.sort(key=lambda arista:arista[0])
    


        dj=self.make_set()
        
        
        

        while len(lista)>0:
            arista=lista[-1]
            lista.pop()
            Peso=arista[0]
            Origen=arista[1]
            Destino=arista[2]

            if self.find_set(Origen, dj)!=self.find_set(Destino, dj):
                g.append(arista)
                self.union(Origen, Destino, dj)
                    
        
        return g








    def make_set(self):
        self.get_list_ady()
        dj=[]
        for nodo in self.__ady:
            dj.append([nodo])
        
        return dj

    def make_set_print(self):
        self.get_list_ady()
        dj=[]
        for nodo in self.__ady:
            dj.append([str(nodo)])
        
        return dj
    

    def find_set(self,nodo,dj):
        i=0
        while i < len(dj):
            if nodo in dj[i]:
                return i

            i=i+1

    def union(self,origen, destino, dj):
        i= self.find_set(origen,dj)
        j=self.find_set(destino,dj)

        l_origen=dj[i]
        l_destino=dj[j]

        l_union=l_origen+l_destino

        dj.remove(l_origen)
        dj.remove(l_destino)
        dj.append(l_union)


    def kruskal_print(self):
        self.get_list_ady()
        g=[]
        lista=[]
        for key in self.__ady.keys():
            for value in self.__ady[key]:
                nodo=value[0]
                peso=value[1]
                arista=(peso, str(key), str(nodo))
                lista.append(arista)
                
        
        lista.sort(key=lambda arista:arista[0])
        
        for arista in lista:

            peso=arista[0]
            origen=arista[1]
            destino=arista[2]
            print(f"{peso}, {origen},{destino}")
        print("\n")


        dj=self.make_set_print()
        print(f"{dj}")
        
        

        while len(lista)>0:
            arista=lista[-1]
            lista.pop()
            Peso=arista[0]
            Origen=arista[1]
            Destino=arista[2]

            if self.find_set(Origen, dj)!=self.find_set(Destino, dj):
                g.append(arista)
                self.union(Origen, Destino, dj)
                print(f"{dj}")

    def dijkstra(self, origen:Nodo):
        distancias = {}
        camino = {}
        for nodo in self.__ady:
            distancias[nodo] = 10000
            camino[nodo] = ""


        distancias[origen] = 0
        camino[origen] = origen
        
        distancia=0
        pq = PriorityQueue()
        pq.put((0, origen))


        while not pq.empty():
        
            nodo = pq.get()
            n = nodo[1]
            
            for arista in self.__ady[n]:
            
                distancia = arista[1] + nodo[0]
                #el destino será la arista en posición 0
                destino = arista[0]
                
                if distancia < distancias[destino]:
                
                    distancias[destino] = distancia
                    
                    camino[destino] = n
                    
                    pq.put((distancia, destino))
        
        return distancias, camino
                            
                
                


                
        
        
        


        
        




        
                

                        

                
                    
            
            
                
                
        
        




        

            

            
            
            
            


          
                
                
                        
                        
                        
        
            
        
        
            

        
        
 
        
    
    
   
                    
            
            
            
        
        
        
    
                
        
    