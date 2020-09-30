from PyQt5 import QtCore, QtGui, QtWidgets
# from utils import return_data,write_data
import sys,platform

def no_abort(a, b, c):
    sys.__excepthook__(a, b, c)
sys.excepthook = no_abort

class ProxiesPage(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(ProxiesPage, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, proxiespage):
        pass