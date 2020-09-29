from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os #,images.images

'''
Contains the original values of excepthook at the start of the program. 
They are saved so that excepthook can be restored in case they happen to
get replaced with broken or alternative objects.
'''
def no_abort(a, b, c):
  '''
  sys.excepthook(type, value, traceback)

  This function prints out a given traceback and exception to sys.stderr.
  '''
  sys.__excepthook__(a, b, c)
sys.excepthook = no_abort

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(1109, 600)
        MainWindow.setStyleSheet("background-color: #1E1E1E;")
        MainWindow.setWindowTitle("Bird Bot Redux")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QMessageBox QLabel { color: #FFFFFF; }QMessageBox QPushButton { background-color: #5D43FB;color: #FFFFFF;}")
        self.sidebar = QtWidgets.QWidget(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(0, 0, 61, 601))
        self.sidebar.setStyleSheet("background-color: #232323;border-right: 1px solid #2e2d2d;")
        self.home_tab = QtWidgets.QWidget(self.sidebar)
        self.home_tab.setGeometry(QtCore.QRect(0, 85, 60, 45))
        self.home_tab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_tab.setStyleSheet("background-color: #272342;border: none;")
        self.home_active_tab = QtWidgets.QWidget(self.home_tab)
        self.home_active_tab.setGeometry(QtCore.QRect(0, 0, 4, 45))
        self.home_active_tab.setStyleSheet("background-color: #5D43FB;border: none;")
        self.home_active_tab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_icon = QtWidgets.QLabel(self.home_tab)
        self.home_icon.setGeometry(QtCore.QRect(21, 13, 20, 20))
        self.home_icon.setStyleSheet("border: none;")
        self.home_icon.setText("")
        self.home_icon.setPixmap(QtGui.QPixmap(":/images/home_alt.png"))
        self.home_icon.setScaledContents(True)
        self.home_icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profiles_tab = QtWidgets.QWidget(self.sidebar)
        self.profiles_tab.setGeometry(QtCore.QRect(0, 130, 60, 45))
        self.profiles_tab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profiles_tab.setStyleSheet("background-color: transparent;border: none;")
        self.profiles_active_tab = QtWidgets.QWidget(self.profiles_tab)
        self.profiles_active_tab.setGeometry(QtCore.QRect(0, 0, 4, 45))
        self.profiles_active_tab.setStyleSheet("background-color: transparent;border: none;")
        self.profiles_active_tab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profiles_icon = QtWidgets.QLabel(self.profiles_tab)
        self.profiles_icon.setGeometry(QtCore.QRect(21, 13, 20, 20))
        self.profiles_icon.setStyleSheet("border: none;")
        self.profiles_icon.setText("")
        self.profiles_icon.setPixmap(QtGui.QPixmap(":/images/profiles.png"))
        self.profiles_icon.setScaledContents(True)
        self.profiles_icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.proxies_tab = QtWidgets.QWidget(self.sidebar)
        self.proxies_tab.setGeometry(QtCore.QRect(0, 175, 60, 45))
        self.proxies_tab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.proxies_tab.setStyleSheet("background-color: transparent;border: none;")
        self.proxies_active_tab = QtWidgets.QWidget(self.proxies_tab)
        self.proxies_active_tab.setGeometry(QtCore.QRect(0, 0, 4, 45))
        self.proxies_active_tab.setStyleSheet("background-color: transparent;border: none;")
        self.proxies_icon = QtWidgets.QLabel(self.proxies_tab)
        self.proxies_icon.setGeometry(QtCore.QRect(21, 13, 20, 20))
        self.proxies_icon.setStyleSheet("border: none;")
        self.proxies_icon.setPixmap(QtGui.QPixmap(":/images/proxies.png"))
        self.proxies_icon.setScaledContents(True)
        self.settings_tab = QtWidgets.QWidget(self.sidebar)
        self.settings_tab.setGeometry(QtCore.QRect(0, 220, 60, 45))
        self.settings_tab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_tab.setStyleSheet("background-color: transparent;border: none;")
        self.settings_active_tab = QtWidgets.QWidget(self.settings_tab)
        self.settings_active_tab.setGeometry(QtCore.QRect(0, 0, 4, 45))
        self.settings_active_tab.setStyleSheet("background-color: transparent;border: none;")
        self.settings_icon = QtWidgets.QLabel(self.settings_tab)
        self.settings_icon.setGeometry(QtCore.QRect(21, 13, 20, 20))
        self.settings_icon.setStyleSheet("border: none;")
        self.settings_icon.setPixmap(QtGui.QPixmap(":/images/settings.png"))
        self.settings_icon.setScaledContents(True)
        self.logo = QtWidgets.QLabel(self.sidebar)
        self.logo.setGeometry(QtCore.QRect(10, 23, 41, 41))
        self.logo.setStyleSheet("border: none;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/images/birdbot.png"))
        self.logo.setScaledContents(True)
        # self.homepage = HomePage(self.centralwidget)
        # self.createdialog = CreateDialog(self)
        # self.createdialog.addtask_btn.clicked.connect(self.create_task)
        # self.createdialog.setWindowIcon(QtGui.QIcon("images/birdbot.png"))
        # self.createdialog.hide()
        # self.profilespage = ProfilesPage(self.centralwidget)
        # self.profilespage.hide()
        # self.proxiespage = ProxiesPage(self.centralwidget)
        # self.proxiespage.hide()
        # self.settingspage = SettingsPage(self.centralwidget)
        # self.settingspage.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    ui_app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.setWindowIcon(QtGui.QIcon("images/birdbot.png"))
    os._exit(ui_app.exec_())