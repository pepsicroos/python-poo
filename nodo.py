class Nodo:
    
    def __init__(self, dato):
        self.__dato = dato
#con la propiedad se accede al dato privado
    @property
    def dato(self):
        return self.__dato
#para convertir a string el nodo
    def __str__(self) -> str:
    #con f le damos formato a lo que vamos a imprimir
        return f"{self.dato}"
#comparamos si el nodo es igual (==)
    def __eq__(self, o: object) -> bool:
        return self.dato == o.dato

    def __hash__(self) -> int:
        return hash(self.dato)
    def get_x(self):
        return self.__dato[0]
    def get_y(self):
        return self.__dato[1]
        
        