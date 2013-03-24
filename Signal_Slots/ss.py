__author__ = 'wil_jm'


import sys
from PyQt4 import QtGui, uic, QtCore

class Demo(QtGui.QMainWindow):

    def __init__(self):
        super(Demo, self).__init__()
        self.var=uic.loadUi('form.ui', self)
        self.connect(self,self.var.pushButton,QtCore.SIGNAL("clicked"),self.mostrar())


    def mostrar(self):
        texto=str(self.var.lineEdit.text())
        print texto

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = Demo()
    ui.show()
    sys.exit(app.exec_())


