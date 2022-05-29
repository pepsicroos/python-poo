from nodo import *
class Arista:
    def __init__(self, n1:Nodo, n2:Nodo) -> None:
        self.__par=[n1,n2]
        
    
    def get_par(self)-> list:
        return self.__par
    
    
    def __str__(self) -> str:
        return f"(Nodo: {self.get_par()[0]}) --- (Nodo: {self.get_par()[1]})"
    
    
    def dirigido(self):
        return False
    
    def ponderado(self):
        return True
    
    def __eq__(self, o: object) -> bool:
        #return self.get_par()[0] == o.get_par()[0] and self.get_par()[1]== o.get_par()[1]
        return self.get_par()[0] == o.get_par()[0] and self.get_par()[1] == o.get_par()[1]
    

class AristaNodirigida(Arista):
    def __init__(self, n1, n2) -> None:
        super().__init__(n1, n2)
    
    
    def dirigido(self):
        return False
    
    def ponderado(self):
        return False
    
    
    def get_nodo1(self):
        return self.get_par()[0]
    
    def get_nodo2(self):
        return self.get_par()[1]
    
    def __str__(self) -> str:
        return f"(Nodo: {self.get_par()[0]}) <---> (Nodo: {self.get_par()[1]})"
        
    


class Ponderada:
    def __init__(self, peso) -> None:
        self.__peso=peso
        
    @property
    def peso(self):
        return self.__peso

class AristaNodirigidaPonderada(AristaNodirigida, Ponderada):
    def __init__(self, n1:Nodo, n2:Nodo, peso) -> None:
        AristaNodirigida.__init__(self, n1,n2)
        Ponderada.__init__(self, peso)
        
    def ponderado(self):
        return True
        
    def __str__(self) -> str:
        return f"(Nodo: {self.get_par()[0]}) <-- {self.peso} --> (Nodo: {self.get_par()[1]})"



class AristaDirigidaPonderada(Arista, Ponderada):
    def __init__(self, n1:Nodo, n2:Nodo, peso) -> None:
        Arista.__init__(self, n1, n2)
        Ponderada.__init__(self, peso)

    def ponderado(self):
        return True

    def dirigido(self):
        return False
    
    def get_nodo1(self):
        return self.get_par()[0]
    
    def get_nodo2(self):
        return self.get_par()[1]
    
    def __str__(self) -> str:
        return f"(Nodo: {self.get_par()[0]}) ---{self.peso} ---> (Nodo: {self.get_par()[1]})"

    #def __eq__(self, o: object) -> bool:
        return self.get_par()[0] == o.get_par()[0] and self.get_par()[1]== o.get_par()[1]
    
        
    

        
    

        
    
    