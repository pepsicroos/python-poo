from algoritmos import distancia_euclidiana


class Particula:

    def __init__(self,id="",origen_x=0,origen_y=0,destino_x=0,destino_y=0,velocidad=0,red=0,green=0,blue=0):
        self.__id=id
        self.__origen_x=origen_x 
        self.__origen_y=origen_y 
        self.__destino_x=destino_x
        self.__destino_y=destino_y 
        self.__velocidad=velocidad 
        self.__red =red 
        self.__green =green 
        self.__blue =blue 
        
        self.distancia =distancia_euclidiana(destino_x,origen_x,destino_y,origen_y)
    



    @property
    def Id(self):
        return self.__id


    @property
    def Origen_x(self):
        return self.__origen_x

    @property
    def Origen_y(self):
        return self.__origen_y


    @property
    def Destino_x(self):
        return self.__destino_x


    @property
    def Destino_y(self):
        return self.__destino_y


    @property
    def Velocidad(self):
        return self.__velocidad


    @property
    def Red(self):
        return self.__red


    @property
    def Green(self):
        return self.__green


    @property
    def Blue(self):
        return self.__blue





    
    def __str__(self):
        return(
            'id: ' + self.__id + '\n'+
            'Origen X: '+ str(self.__origen_x) + '\n' +
            'Origen Y: '+ str(self.__origen_y) + '\n' +
            'Destino X: '+ str(self.__destino_x) + '\n' +
            'Destino Y: '+str(self.__destino_y) + '\n' +
            'Velocidad: '+str(self.__velocidad) + '\n' +
            'Red: '+ str(self.__red) + '\n' +
            'Green: '+ str(self.__green) + '\n' +
            'Blue: '+str(self.__blue) + '\n' +
            'Distancia: '+ str(self.distancia) + '\n'

        )
    

    def to_dict(self):
        return{
            "id":self.__id,
            "origen_x":self.__origen_x,
            "origen_y":self.__origen_y,
            "destino_x":self.__destino_x,
            "destino_y":self.__destino_y,
            "velocidad":self.__velocidad,
            "red":self.__red,
            "green":self.__green,
            "blue":self.__blue
        }

    def sortby_id(part):
        parts=Particula()
        return parts.Id
        



        
        