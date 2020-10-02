from PyQt5 import QtCore, QtGui, QtWidgets
import sys, platform


def no_abort(a, b, c):
    sys.__excepthook__(a, b, c)


sys.excepthook = no_abort


class CreateDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CreateDialog, self).__init__(parent)
        self.setupUi(self)
        self.show()

    def setupUi(self, CreateDialog):
        self.CreateDialog = CreateDialog
        CreateDialog.setFixedSize(647, 164)
        CreateDialog.setStyleSheet(
            "QComboBox::drop-down {    border: 0px;}QComboBox::down-arrow {    image: url(:/images/down_icon.png);    width: 14px;    height: 14px;}QComboBox{    padding: 1px 0px 1px 3px;}QLineEdit:focus {   border: none;   outline: none;} QSpinBox::up-button {subcontrol-origin: border;subcontrol-position: top right;width: 8px; border-image: url(:/images/uparrow_icon.png) 1;border-width: 1px;}QSpinBox::down-button {subcontrol-origin: border;subcontrol-position: bottom right;width: 8px;border-image: url(:/images/downarrow_icon.png) 1;border-width: 1px;border-top-width: 0;}"
        )
        CreateDialog.setWindowTitle("Create Tasks")

        self.background = QtWidgets.QWidget(CreateDialog)
        self.background.setGeometry(QtCore.QRect(0, 0, 691, 391))
        self.background.setStyleSheet("background-color: #1E1E1E;")

        font = QtGui.QFont()
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(
            13 * 0.75
        )
        font.setFamily("Arial")
        self.site_box = QtWidgets.QComboBox(self.background)
        self.site_box.setGeometry(QtCore.QRect(50, 20, 151, 21))
        self.site_box.setStyleSheet(
            "outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);"
        )
        self.site_box.addItem("Site")
        self.site_box.setFont(font)
        self.site_box.addItem("Bestbuy")
        self.site_box.addItem("Walmart")
        self.input_edit = QtWidgets.QLineEdit(self.background)
        self.input_edit.setGeometry(QtCore.QRect(250, 20, 151, 21))
        self.input_edit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input_edit.setStyleSheet(
            "outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);"
        )
        self.input_edit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.input_edit.setPlaceholderText("Link")
        self.input_edit.setFont(font)
        self.input_edit.textEdited.connect(self.autofill)
        self.profile_box = QtWidgets.QComboBox(self.background)
        self.profile_box.setGeometry(QtCore.QRect(450, 20, 151, 21))
        self.profile_box.setStyleSheet(
            "outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);"
        )
        self.profile_box.addItem("Profile")
        self.profile_box.setFont(font)
        self.proxies_box = QtWidgets.QComboBox(self.background)
        self.proxies_box.setGeometry(QtCore.QRect(450, 70, 151, 21))
        self.proxies_box.setStyleSheet(
            "outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);"
        )
        self.proxies_box.addItem("Proxy List")
        self.proxies_box.addItem("None")
        self.proxies_box.setFont(font)
        self.monitor_edit = QtWidgets.QLineEdit(self.background)
        self.monitor_edit.setGeometry(QtCore.QRect(50, 70, 61, 21))
        self.monitor_edit.setStyleSheet(
            "outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);"
        )
        self.monitor_edit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.monitor_edit.setPlaceholderText("Monitor")
        self.monitor_edit.setFont(font)
        self.monitor_edit.setText("5.0")
        self.only_float = QtGui.QDoubleValidator()
        self.monitor_edit.setValidator(self.only_float)
        self.error_edit = QtWidgets.QLineEdit(self.background)
        self.error_edit.setGeometry(QtCore.QRect(140, 70, 61, 21))
        self.error_edit.setStyleSheet(
            "outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);"
        )
        self.error_edit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.error_edit.setPlaceholderText("Error")
        self.error_edit.setFont(font)
        self.error_edit.setText("5.0")
        self.error_edit.setValidator(self.only_float)
        self.addtask_btn = QtWidgets.QPushButton(self.background)
        self.addtask_btn.setGeometry(QtCore.QRect(250, 110, 151, 32))
        self.addtask_btn.setText("Add Task")
        self.maxprice_checkbox = QtWidgets.QCheckBox(self.background)
        self.maxprice_checkbox.setGeometry(QtCore.QRect(250, 70, 87, 20))
        font = QtGui.QFont()
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(
            13 * 0.75
        )
        font.setFamily("Arial")
        self.maxprice_checkbox.setFont(font)
        self.maxprice_checkbox.setStyleSheet("color: #FFFFFF;")
        self.maxprice_checkbox.setText("Max Price")
        self.price_edit = QtWidgets.QLineEdit(self.background)
        self.price_edit.setGeometry(QtCore.QRect(350, 70, 51, 21))
        self.price_edit.setFont(font)
        self.price_edit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.price_edit.setStyleSheet(
            "outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);"
        )
        self.price_edit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.only_int = QtGui.QIntValidator()
        self.price_edit.setValidator(self.only_int)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14) if platform.system() == "Darwin" else font.setPointSize(
            14 * 0.75
        )
        self.addtask_btn.setFont(font)
        self.addtask_btn.setStyleSheet(
            "border-radius: 10px;background-color: #5D43FB;color: #FFFFFF;"
        )
        self.addtask_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.taskcount_spinbox = QtWidgets.QSpinBox(self.background)
        self.taskcount_spinbox.setGeometry(QtCore.QRect(420, 115, 41, 21))
        self.taskcount_spinbox.setStyleSheet(
            "border: 1px solid #5D43FB;border-width: 0 0 2px;color: #FFFFFF;"
        )
        self.taskcount_spinbox.setMinimum(1)
        self.taskcount_spinbox.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)

        QtCore.QMetaObject.connectSlotsByName(CreateDialog)

    def autofill(self):
        if "bestbuy" in self.input_edit.text():
            self.site_box.setCurrentIndex(self.site_box.findText("Bestbuy"))
        elif "walmart" in self.input_edit.text():
            self.site_box.setCurrentIndex(self.site_box.findText("Walmart"))

    def load_data(self, task_tab):
        self.site_box.setCurrentText(task_tab.site)
        self.input_edit.setText(task_tab.product)
        self.profile_box.setCurrentText(task_tab.profile)
        self.proxies_box.setCurrentText(task_tab.proxies)
        self.monitor_edit.setText(task_tab.monitor_delay)
        self.error_edit.setText(task_tab.error_delay)
        self.price_edit.setText(task_tab.max_price)
        self.maxprice_checkbox.setChecked(task_tab.max_price is not "")
        self.addtask_btn.setText("Update Task")
