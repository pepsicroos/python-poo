import math



def distancia_euclidiana(x_2,x_1, y_2, y_1):
    resultadoDistancia=math.sqrt((x_2-x_1)**2+ (y_2-y_1)**2)
    return resultadoDistancia


def puntos_mas_cercano(puntos:list) -> list:
    resultado=[]
    for punto_i in puntos:
        x1=punto_i[0]
        y1=punto_i[1]
       

        min=1000
       
        cercano=(0,0)
        for punto_j in puntos:
            if(punto_i!=punto_j):
                x2=punto_j[0]
                y2=punto_j[1]
                

                d=distancia_euclidiana(x2,x1,y2,y1)
                if(d<min):
                    min=d
                    cercano=(x2,y2)


        
        resultado.append((punto_i,cercano))
    
    return resultado
    
