from PyQt5 import QtCore, QtGui, QtWidgets
# from utils import return_data,write_data,get_profile,Encryption
import sys,platform

def no_abort(a, b, c):
    sys.__excepthook__(a, b, c)
sys.excepthook = no_abort

class ProfilesPage(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(ProfilesPage, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, profilespage):
        pass