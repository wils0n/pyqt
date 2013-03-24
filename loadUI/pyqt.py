import sys
from PyQt4 import QtGui, uic

class Demo(QtGui.QMainWindow):

    def __init__(self):
        super(Demo, self).__init__()
        uic.loadUi('test.ui', self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = Demo()
    ui.show()
    sys.exit(app.exec_())



#al cargar el archivo.ui se carga con todo signals and slots que se ha hecho en qtDesigner
