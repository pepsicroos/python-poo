from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QFileDialog,QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from algoritmos import puntos_mas_cercano
from pymainwindow import Ui_MainWindow
from administraParticula import *
from particula import *
from nodo import *
from arista import *
from grafo import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.particulaa=AdministraParticulas()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.puntos=[]

        self.ui.agregafinal_pushButton.clicked.connect(self.agregarFinal)
        self.ui.agregainicio_pushbutton.clicked.connect(self.agregarInicio)
        self.ui.Dibuja_pushButton.clicked.connect(self.clickdibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpia)
        self.ui.produndidad_pushbutton.clicked.connect(self.recorre_profundidad)
        self.ui.anchura_pushbutton.clicked.connect(self.recorre_amplitud)
        self.ui.mostrar_pushbutton.clicked.connect(self.clickmostrar)
        self.ui.actionAbrir.triggered.connect(self.abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.guarda_archivo)
        self.ui.mostrar_tabla_pushButton_2.clicked.connect(self.muestra_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.busca_particula)
        self.ui.ordena_id_pushButton.clicked.connect(self.clickOrdenarID)
        self.ui.pordena_vel_pushButton.clicked.connect(self.clickOrdenarVel)
        self.ui.Ordana_dist_pushButton.clicked.connect(self.clickOrdenarDist)
        self.ui.MuestraPuntos_pushButton.clicked.connect(self.muestra_puntos)
        self.ui.fuerza_bruta_pushButton.clicked.connect(self.calcula_puntos_cercanos)
        self.ui.grafo_pushButton.clicked.connect(self.agrega_part_grafo)
        self.ui.Prim_pushButton.clicked.connect(self.encuentra_prim)
        self.ui.kruskal_pushButton.clicked.connect(self.algoritmo_kruskal)
        self.ui.dikjstra_pushButton.clicked.connect(self.algoritmo_dijkstra)
        self.scene=QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)


    @Slot()
    def calcula_puntos_cercanos(self):
        resultado=puntos_mas_cercano(self.puntos)
        
        for punto1,punto2 in resultado:
            x1=punto1[0]
            y1=punto1[1]
            x2=punto2[0]
            y2=punto2[1]

            self.scene.addLine(x1+3,y1+3,x2+3,y2+3)

    @Slot()
    def abrir_archivo(self):
        ubicacion=QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if(self.particulaa.abrir(ubicacion)):
            QMessageBox.information(
            self,
            "Exito",
            "Se pudo abrir el archivo"+ ubicacion
            )
            
            
            pen=QPen()
            pen.setWidth(2)
            for part in self.particulaa:
                ox=part.Origen_x
                oy=part.Origen_y
                dx=part.Destino_x
                dy=part.Destino_y
                r=part.Red
                g=part.Green
                b=part.Blue
                color=QColor(r, g,b)
                pen.setColor(color)
                
                self.scene.addEllipse(ox,oy, 3,3, pen)
                self.scene.addEllipse(dx,dy, 3,3, pen)
                self.scene.addLine(ox,oy,dx,dy,pen)

        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo abrir el archivo"+ ubicacion
            )
            print(Particula)

        
    




    @Slot()
    def guarda_archivo(self):
        ubicacion=QFileDialog.getSaveFileName(
            self,
            'Guardar archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if(self.particulaa.guardar(ubicacion)):
            QMessageBox.information(
            self,
            "Exito",
            "Se pudo crear el archivo"+ ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo"+ ubicacion
            )






    @Slot()
    def agregarFinal(self):
        


        Id=self.ui.ID_lineEdit.text()
        origen_x=self.ui.origen_x_spinBox.value()
        origen_y=self.ui.origen_y_spinBox.value()
        destino_x=self.ui.destinox.value()
        destino_y=self.ui.destinoy.value()
        velocidad=self.ui.velocidad.value()
        red=self.ui.red.value()
        green=self.ui.green.value()
        blue=self.ui.blue.value()

        part=Particula(Id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.particulaa.agregaFinal(part)

        
        
        







    @Slot()
    def agregarInicio(self):

        Id=self.ui.ID_lineEdit.text()
        origen_x=self.ui.origen_x_spinBox.value()
        origen_y=self.ui.origen_y_spinBox.value()
        destino_x=self.ui.destinox.value()
        destino_y=self.ui.destinoy.value()
        velocidad=self.ui.velocidad.value()
        red=self.ui.red.value()
        green=self.ui.green.value()
        blue=self.ui.blue.value()

        part=Particula(Id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.particulaa.agregaInicio(part)

        
        
        
        




    @Slot()
    def clickmostrar(self):
        
        self.particulaa.mostrar()
        self.ui.salidatexto.clear()
        self.ui.salidatexto.insertPlainText(str(self.particulaa))


    @Slot()
    def limpia(self):
        self.scene.clear()

    @Slot()
    def clickOrdenarID(self):
        self.particulaa.ordenapor_ID()

    
    @Slot()
    def clickOrdenarVel(self):
        self.particulaa.ordenaporVelocidad()

    
    @Slot()
    def clickOrdenarDist(self):
        self.particulaa.ordenaporDistancia()
        



    @Slot()
    def muestra_tabla(self):
        self.ui.tableWidget.setColumnCount(10)
        headers=["id","Origen X","Origen Y","Destino X","Destino Y","Velocidad","Red","Green","Blue","Distancia"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

        self.ui.tableWidget.setRowCount(len(self.particulaa))


        row=0
        for part in self.particulaa:
            idwidget=QTableWidgetItem(str(part.Id))
            origenX_widget=QTableWidgetItem(str(part.Origen_x))
            origenY_widget=QTableWidgetItem(str(part.Origen_y))
            destinoX_widget=QTableWidgetItem(str(part.Destino_x))
            destinoY_widget=QTableWidgetItem(str(part.Destino_y))
            velocidad_widget=QTableWidgetItem(str(part.Velocidad))
            red_widget=QTableWidgetItem(str(part.Red))
            greee_widget=QTableWidgetItem(str(part.Green))
            blue_widget=QTableWidgetItem(str(part.Blue))
            distancia_widget=QTableWidgetItem(str(part.distancia))

            self.ui.tableWidget.setItem(row,0,idwidget)
            self.ui.tableWidget.setItem(row,1,origenX_widget)
            self.ui.tableWidget.setItem(row,2,origenY_widget)
            self.ui.tableWidget.setItem(row,3,destinoX_widget)
            self.ui.tableWidget.setItem(row,4,destinoY_widget)
            self.ui.tableWidget.setItem(row,5,velocidad_widget)
            self.ui.tableWidget.setItem(row,6,red_widget)
            self.ui.tableWidget.setItem(row,7,greee_widget)
            self.ui.tableWidget.setItem(row,8,blue_widget)
            self.ui.tableWidget.setItem(row,9,distancia_widget)

            row +=1


    

    @Slot()
    def busca_particula(self):
        Idbusca=self.ui.bucar_lineEdit.text()

        encontrado=False
        for part in self.particulaa:
            if(Idbusca == part.Id):
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setColumnCount(10)
                headers=["id","Origen X","Origen Y","Destino X","Destino Y","Velocidad","Red","Green","Blue","Distancia"]
                self.ui.tableWidget.setHorizontalHeaderLabels(headers)
                self.ui.tableWidget.setRowCount(1)
                idwidget=QTableWidgetItem(str(part.Id))
                origenX_widget=QTableWidgetItem(str(part.Origen_x))
                origenY_widget=QTableWidgetItem(str(part.Origen_y))
                destinoX_widget=QTableWidgetItem(str(part.Destino_x))
                destinoY_widget=QTableWidgetItem(str(part.Destino_y))
                velocidad_widget=QTableWidgetItem(str(part.Velocidad))
                red_widget=QTableWidgetItem(str(part.Red))
                greee_widget=QTableWidgetItem(str(part.Green))
                blue_widget=QTableWidgetItem(str(part.Blue))
                distancia_widget=QTableWidgetItem(str(part.distancia))

                self.ui.tableWidget.setItem(0,0,idwidget)
                self.ui.tableWidget.setItem(0,1,origenX_widget)
                self.ui.tableWidget.setItem(0,2,origenY_widget)
                self.ui.tableWidget.setItem(0,3,destinoX_widget)
                self.ui.tableWidget.setItem(0,4,destinoY_widget)
                self.ui.tableWidget.setItem(0,5,velocidad_widget)
                self.ui.tableWidget.setItem(0,6,red_widget)
                self.ui.tableWidget.setItem(0,7,greee_widget)
                self.ui.tableWidget.setItem(0,8,blue_widget)
                self.ui.tableWidget.setItem(0,9,distancia_widget)

                encontrado=True
                return
            
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'Particula "{Idbusca}" no encontrada'
            )

    @Slot()
    def clickdibujar(self):
        pen=QPen()
        pen.setWidth(2)

        
        origen_x=self.ui.origen_x_spinBox.value()
        origen_y=self.ui.origen_y_spinBox.value()
        destino_x=self.ui.destinox.value()
        destino_y=self.ui.destinoy.value()
        red=self.ui.red.value()
        green=self.ui.green.value()
        blue=self.ui.blue.value()


        color=QColor(red, green, blue)
        pen.setColor(color)

        
        self.scene.addEllipse(origen_x,origen_y, 3,3, pen)
        self.scene.addEllipse(destino_x,destino_y, 3,3, pen)
        self.scene.addLine(origen_x,origen_y,destino_x,destino_y,pen)

    
    def getpuntos(self) ->list:
        puntos=[]
        

        for part in self.particulaa:
            ox=part.Origen_x
            oy=part.Origen_y
            dx=part.Destino_x
            dy=part.Destino_y

            punto_o=(ox,oy)
            punto_d=(dx,dy)
            puntos.append(punto_o)
            puntos.append(punto_d)
            
        
        return puntos
    

    @Slot()
    def muestra_puntos(self):
        self.puntos=self.getpuntos()

        for punto in self.puntos:
            x1=punto[0]
            y1=punto[1]
            
            self.scene.addEllipse(x1,y1, 3,3)
    
    
    @Slot()
    def agrega_part_grafo(self):
        g=Grafo()
        for part in self.particulaa:
            ox=part.Origen_x
            oy=part.Origen_y
            dx=part.Destino_x
            dy=part.Destino_y
            
            n1=Nodo((ox,oy))
            n2=Nodo((dx,dy))
            arista=AristaNodirigida(n1,n2)
            g.agrega_arista(arista)
        g.print_ady()
        self.ui.salidatexto.clear()
        self.ui.salidatexto.insertPlainText(g.string_window())
        
        
            
        
    @Slot()
    def recorre_profundidad(self):
        cadena=""
        g=Grafo()
        origen_x=self.ui.origen_x_spinBox_2.value()
        origen_y=self.ui.origen_y_spinBox_2.value()
        punto_ref=Nodo((origen_x,origen_y))
        for part in self.particulaa:
            ox=part.Origen_x
            oy=part.Origen_y
            dx=part.Destino_x
            dy=part.Destino_y
            
            n1=Nodo((ox,oy))
            n2=Nodo((dx,dy))
            arista=AristaNodirigida(n1,n2)
            g.agrega_arista(arista)
        if (origen_x or origen_y) == None or g.get_key(punto_ref)==False:
            #arroja ventana con mensaje
            QMessageBox.critical(
                self, 
                "No es posible realizar el recorrido",
                "Deposita valores validos"
            )
        else:
            
            
            punto_ref=Nodo((origen_x,origen_y))
            print("Origen: ",punto_ref)
            cadena="Origen: "+str(punto_ref)+'\n'
            print("Recorrido en profundidad")
            cadena+="Recorrido en profundidad"+'\n'
            for n in g.recorrido_profundidad(punto_ref):
                print(n)
                cadena+=str(n)+'\n'
            
            print("\n")
            cadena+='\n'
            self.ui.salidatexto.clear()
            self.ui.salidatexto.insertPlainText(cadena)
        
    
    @Slot()
    def recorre_amplitud(self):
        cadena=""
        g=Grafo()
        origen_x=self.ui.origen_x_spinBox_3.value()
        origen_y=self.ui.origen_y_spinBox_3.value()
        punto_ref=Nodo((origen_x,origen_y))
        for part in self.particulaa:
            ox=part.Origen_x
            oy=part.Origen_y
            dx=part.Destino_x
            dy=part.Destino_y
            
            n1=Nodo((ox,oy))
            n2=Nodo((dx,dy))
            arista=AristaNodirigida(n1,n2)
            g.agrega_arista(arista)
        
        if (origen_x or origen_y) == None or g.get_key(punto_ref)==False:
            #arroja ventana con mensaje
            QMessageBox.critical(
                self, 
                "No es posible realizar el recorrido",
                "Deposita valores validos"
            )
        else:
            
            print("Origen: ",punto_ref)
            cadena="Origen: "+str(punto_ref)+'\n'
            cadena+="Recorrido en amplitud"+'\n'
            print("Recorrido en amplitud")
            for n in g.recorrido_amplitud(punto_ref):
                print(n)
                cadena+=str(n)+'\n'
            
            print("\n")
            cadena+='\n'
            self.ui.salidatexto.clear()
            self.ui.salidatexto.insertPlainText(cadena)
    
    
    @Slot()
    def encuentra_prim(self):
        g=Grafo()
        origen_x=self.ui.origen_x_spinBox_4.value()
        origen_y=self.ui.origen_y_spinBox_4.value()
        inicio=Nodo((origen_x,origen_y))
        for part in self.particulaa:
            ox=part.Origen_x
            oy=part.Origen_y
            dx=part.Destino_x
            dy=part.Destino_y
            peso=part.distancia
            

            n1=Nodo((ox,oy))
            n2=Nodo((dx,dy))

            arista=AristaNodirigidaPonderada(n1,n2,peso)
            g.agrega_arista(arista)
        pen = QPen()
        pen.setWidth(10)
        color = QColor(255, 0, 0)
        pen.setColor(color)
        prim=g.algoritmo_prim(inicio)
        for arista in prim:

            origen=arista[1].dato
            destino=arista[2].dato

            x1=origen[0]
            y1=origen[1]
            x2=destino[0]
            y2=destino[1]


            
        
            self.scene.addLine(x1+3, y1+3,x2+3,y2+3, pen)
    

    @Slot()
    def algoritmo_kruskal(self):
        g=Grafo()
        for part in self.particulaa:
            ox=part.Origen_x
            oy=part.Origen_y
            dx=part.Destino_x
            dy=part.Destino_y
            peso=part.Velocidad
            

            n1=Nodo((ox,oy))
            n2=Nodo((dx,dy))

            arista=AristaNodirigidaPonderada(n1,n2,peso)
            g.agrega_arista(arista)
        arbol=g.kruskal()
        g.kruskal_print()
        for arista_t in arbol:

            peso=arista_t[0]
            origen=arista_t[1].dato
            destino=arista_t[2].dato
            print(f"{origen}: [{peso},{destino}]")
        
        pen = QPen()
        pen.setWidth(10)
        color = QColor(255, 0, 0)
        pen.setColor(color)
        for arista in arbol:


            origen=arista[1].dato
            destino=arista[2].dato

            x1=origen[0]
            y1=origen[1]
            x2=destino[0]
            y2=destino[1]


            
        
            self.scene.addLine(x1+3, y1+3,x2+3,y2+3, pen)
    



    @Slot()
    def algoritmo_dijkstra(self):
        g=Grafo()
        origen_x=int(self.ui.origen_x_spinBox_5.value())
        origen_y=int(self.ui.origen_y_spinBox_5.value())
        inicio=Nodo((origen_x,origen_y))
        destino_x=int(self.ui.destino_x_spinBox_6.value())
        destino_y=int(self.ui.destino_y_spinBox_6.value())
        
        for part in self.particulaa:
            ox=part.Origen_x
            oy=part.Origen_y
            dx=part.Destino_x
            dy=part.Destino_y
            peso=part.distancia
            

            n1=Nodo((ox,oy))
            n2=Nodo((dx,dy))

            arista=AristaDirigidaPonderada(n1,n2,peso)
            g.agrega_arista(arista)
        pen = QPen()
        pen.setWidth(10)
        color = QColor(255, 0, 0)
        pen.setColor(color)
        g.get_list_ady()
        dj=g.dijkstra(inicio)
        camino=dj[1]
        destino=(destino_x,destino_y)
        next = Nodo(destino)
        self.scene.clear()
        while next != Nodo((origen_x,origen_y)):
            actual = camino[next]
            self.scene.addLine(actual.get_x()+3, actual.get_y()+3, next.get_x()+3, next.get_y()+3, pen)
            next = camino[next]
        distancias=dj[0]
        for nodo, value in distancias.items():
            print(nodo, ":", value)
        print('\n')
        for nodo, value in camino.items():
            print(nodo, ":", value)

        
            




            
        
            

        
        
               

