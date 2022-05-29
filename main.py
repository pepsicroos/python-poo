from PySide2.QtWidgets import  QApplication
import sys
from mainwindow import *


app = QApplication()


window=MainWindow()
window.show()

# Qt loops
sys.exit(app.exec_())


