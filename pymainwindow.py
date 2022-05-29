# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(724, 598)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 10, 691, 541))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.salidatexto = QPlainTextEdit(self.tab)
        self.salidatexto.setObjectName(u"salidatexto")
        self.salidatexto.setGeometry(QRect(9, 9, 321, 361))
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(340, 10, 331, 171))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.red = QSpinBox(self.frame)
        self.red.setObjectName(u"red")
        self.red.setMaximum(255)
        self.red.setValue(0)

        self.gridLayout.addWidget(self.red, 3, 1, 1, 2)

        self.velocidad = QSpinBox(self.frame)
        self.velocidad.setObjectName(u"velocidad")
        self.velocidad.setMaximum(9999)
        self.velocidad.setValue(0)

        self.gridLayout.addWidget(self.velocidad, 4, 2, 1, 1)

        self.destinoy = QSpinBox(self.frame)
        self.destinoy.setObjectName(u"destinoy")
        self.destinoy.setMaximum(500)
        self.destinoy.setValue(0)

        self.gridLayout.addWidget(self.destinoy, 2, 5, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 5, 1, 1)

        self.blue = QSpinBox(self.frame)
        self.blue.setObjectName(u"blue")
        self.blue.setMaximum(255)
        self.blue.setValue(0)

        self.gridLayout.addWidget(self.blue, 3, 6, 1, 1)

        self.origen_x_spinBox = QSpinBox(self.frame)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origen_x_spinBox, 1, 2, 1, 1)

        self.green = QSpinBox(self.frame)
        self.green.setObjectName(u"green")
        self.green.setMaximum(255)
        self.green.setValue(0)

        self.gridLayout.addWidget(self.green, 3, 4, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 4, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.ID_lineEdit = QLineEdit(self.frame)
        self.ID_lineEdit.setObjectName(u"ID_lineEdit")

        self.gridLayout.addWidget(self.ID_lineEdit, 0, 2, 1, 5)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 4, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 2)

        self.origen_y_spinBox = QSpinBox(self.frame)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origen_y_spinBox, 1, 5, 1, 1)

        self.destinox = QSpinBox(self.frame)
        self.destinox.setObjectName(u"destinox")
        self.destinox.setAutoFillBackground(False)
        self.destinox.setMaximum(500)
        self.destinox.setValue(0)

        self.gridLayout.addWidget(self.destinox, 2, 2, 1, 1)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(340, 190, 331, 171))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Ordana_dist_pushButton = QPushButton(self.frame_2)
        self.Ordana_dist_pushButton.setObjectName(u"Ordana_dist_pushButton")

        self.gridLayout_4.addWidget(self.Ordana_dist_pushButton, 0, 1, 1, 1)

        self.mostrar_pushbutton = QPushButton(self.frame_2)
        self.mostrar_pushbutton.setObjectName(u"mostrar_pushbutton")

        self.gridLayout_4.addWidget(self.mostrar_pushbutton, 5, 0, 1, 1)

        self.grafo_pushButton = QPushButton(self.frame_2)
        self.grafo_pushButton.setObjectName(u"grafo_pushButton")

        self.gridLayout_4.addWidget(self.grafo_pushButton, 5, 1, 1, 1)

        self.ordena_id_pushButton = QPushButton(self.frame_2)
        self.ordena_id_pushButton.setObjectName(u"ordena_id_pushButton")

        self.gridLayout_4.addWidget(self.ordena_id_pushButton, 6, 0, 1, 1)

        self.agregainicio_pushbutton = QPushButton(self.frame_2)
        self.agregainicio_pushbutton.setObjectName(u"agregainicio_pushbutton")

        self.gridLayout_4.addWidget(self.agregainicio_pushbutton, 0, 0, 1, 1)

        self.agregafinal_pushButton = QPushButton(self.frame_2)
        self.agregafinal_pushButton.setObjectName(u"agregafinal_pushButton")

        self.gridLayout_4.addWidget(self.agregafinal_pushButton, 4, 0, 1, 1)

        self.pordena_vel_pushButton = QPushButton(self.frame_2)
        self.pordena_vel_pushButton.setObjectName(u"pordena_vel_pushButton")

        self.gridLayout_4.addWidget(self.pordena_vel_pushButton, 4, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(420, 380, 127, 108))
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)

        self.origen_x_spinBox_2 = QSpinBox(self.groupBox)
        self.origen_x_spinBox_2.setObjectName(u"origen_x_spinBox_2")
        self.origen_x_spinBox_2.setMaximum(500)

        self.gridLayout_7.addWidget(self.origen_x_spinBox_2, 0, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 1, 0, 1, 1)

        self.origen_y_spinBox_2 = QSpinBox(self.groupBox)
        self.origen_y_spinBox_2.setObjectName(u"origen_y_spinBox_2")
        self.origen_y_spinBox_2.setMaximum(500)

        self.gridLayout_7.addWidget(self.origen_y_spinBox_2, 1, 1, 1, 1)

        self.produndidad_pushbutton = QPushButton(self.groupBox)
        self.produndidad_pushbutton.setObjectName(u"produndidad_pushbutton")

        self.gridLayout_7.addWidget(self.produndidad_pushbutton, 2, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(560, 380, 108, 108))
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 1)

        self.origen_x_spinBox_3 = QSpinBox(self.groupBox_2)
        self.origen_x_spinBox_3.setObjectName(u"origen_x_spinBox_3")
        self.origen_x_spinBox_3.setMaximum(500)

        self.gridLayout_6.addWidget(self.origen_x_spinBox_3, 0, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)

        self.origen_y_spinBox_3 = QSpinBox(self.groupBox_2)
        self.origen_y_spinBox_3.setObjectName(u"origen_y_spinBox_3")
        self.origen_y_spinBox_3.setMaximum(500)

        self.gridLayout_6.addWidget(self.origen_y_spinBox_3, 1, 1, 1, 1)

        self.anchura_pushbutton = QPushButton(self.groupBox_2)
        self.anchura_pushbutton.setObjectName(u"anchura_pushbutton")

        self.gridLayout_6.addWidget(self.anchura_pushbutton, 2, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(310, 380, 104, 108))
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)

        self.origen_x_spinBox_4 = QSpinBox(self.groupBox_3)
        self.origen_x_spinBox_4.setObjectName(u"origen_x_spinBox_4")
        self.origen_x_spinBox_4.setMaximum(500)

        self.gridLayout_5.addWidget(self.origen_x_spinBox_4, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 1)

        self.origen_y_spinBox_4 = QSpinBox(self.groupBox_3)
        self.origen_y_spinBox_4.setObjectName(u"origen_y_spinBox_4")
        self.origen_y_spinBox_4.setMaximum(500)

        self.gridLayout_5.addWidget(self.origen_y_spinBox_4, 1, 1, 1, 1)

        self.Prim_pushButton = QPushButton(self.groupBox_3)
        self.Prim_pushButton.setObjectName(u"Prim_pushButton")

        self.gridLayout_5.addWidget(self.Prim_pushButton, 2, 0, 1, 2)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(223, 380, 81, 108))
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.kruskal_pushButton = QPushButton(self.groupBox_4)
        self.kruskal_pushButton.setObjectName(u"kruskal_pushButton")

        self.gridLayout_8.addWidget(self.kruskal_pushButton, 0, 0, 1, 2)

        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 380, 199, 108))
        self.gridLayout_9 = QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_9.addWidget(self.label_16, 0, 0, 1, 1)

        self.origen_x_spinBox_5 = QSpinBox(self.groupBox_5)
        self.origen_x_spinBox_5.setObjectName(u"origen_x_spinBox_5")
        self.origen_x_spinBox_5.setMaximum(500)

        self.gridLayout_9.addWidget(self.origen_x_spinBox_5, 0, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_9.addWidget(self.label_19, 0, 2, 1, 1)

        self.destino_x_spinBox_6 = QSpinBox(self.groupBox_5)
        self.destino_x_spinBox_6.setObjectName(u"destino_x_spinBox_6")
        self.destino_x_spinBox_6.setMaximum(500)

        self.gridLayout_9.addWidget(self.destino_x_spinBox_6, 0, 3, 1, 1)

        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_9.addWidget(self.label_17, 1, 0, 1, 1)

        self.origen_y_spinBox_5 = QSpinBox(self.groupBox_5)
        self.origen_y_spinBox_5.setObjectName(u"origen_y_spinBox_5")
        self.origen_y_spinBox_5.setMaximum(500)

        self.gridLayout_9.addWidget(self.origen_y_spinBox_5, 1, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_9.addWidget(self.label_18, 1, 2, 1, 1)

        self.destino_y_spinBox_6 = QSpinBox(self.groupBox_5)
        self.destino_y_spinBox_6.setObjectName(u"destino_y_spinBox_6")
        self.destino_y_spinBox_6.setMaximum(500)

        self.gridLayout_9.addWidget(self.destino_y_spinBox_6, 1, 3, 1, 1)

        self.dikjstra_pushButton = QPushButton(self.groupBox_5)
        self.dikjstra_pushButton.setObjectName(u"dikjstra_pushButton")

        self.gridLayout_9.addWidget(self.dikjstra_pushButton, 2, 0, 1, 4)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Dibuja_pushButton = QPushButton(self.tab_3)
        self.Dibuja_pushButton.setObjectName(u"Dibuja_pushButton")

        self.gridLayout_3.addWidget(self.Dibuja_pushButton, 1, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.limpiar_pushButton = QPushButton(self.tab_3)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_3.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.MuestraPuntos_pushButton = QPushButton(self.tab_3)
        self.MuestraPuntos_pushButton.setObjectName(u"MuestraPuntos_pushButton")

        self.gridLayout_3.addWidget(self.MuestraPuntos_pushButton, 2, 0, 1, 1)

        self.fuerza_bruta_pushButton = QPushButton(self.tab_3)
        self.fuerza_bruta_pushButton.setObjectName(u"fuerza_bruta_pushButton")

        self.gridLayout_3.addWidget(self.fuerza_bruta_pushButton, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(self.tab_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.bucar_lineEdit = QLineEdit(self.tab_2)
        self.bucar_lineEdit.setObjectName(u"bucar_lineEdit")

        self.gridLayout_2.addWidget(self.bucar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_2.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton_2 = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton_2.setObjectName(u"mostrar_tabla_pushButton_2")

        self.gridLayout_2.addWidget(self.mostrar_tabla_pushButton_2, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 724, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"blue ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"origen y", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"destino x", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"green ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"red ", None))
        self.ID_lineEdit.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"velocidad ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"destino y", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"origen x", None))
        self.Ordana_dist_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordena por distancia", None))
        self.mostrar_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.grafo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imprime grafo Adyacente", None))
        self.ordena_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordena por id", None))
        self.agregainicio_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.agregafinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.pordena_vel_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordena por velocidad", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Recorrido Profundidad", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"origen x", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"origen y", None))
        self.produndidad_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Recorre profundidad", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Recorrido Anchura", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"origen x", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"origen y", None))
        self.anchura_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Recorre anchura", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmo Prim", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"origen x", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"origen y", None))
        self.Prim_pushButton.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.kruskal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Dijkstra ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"origen x", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"destino x", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"origen y", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"destino y", None))
        self.dikjstra_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dijkstra ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Dibuja_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibuja particulas", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"limpiar", None))
        self.MuestraPuntos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar puntos", None))
        self.fuerza_bruta_pushButton.setText(QCoreApplication.translate("MainWindow", u"Calcula puntos mas cercanos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Mostrar particula", None))
        self.bucar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID PARTICULA", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

