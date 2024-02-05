from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys
import UI.login.login_rc


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.loadLoginUI()
        self.show()

    def loadLoginUI(self):
        uic.loadUi("UI/login/login.ui", self)
        self.registerButton.clicked.connect(self.loadFunctionCourse)

app = QApplication(sys.argv)
window = App()
app.exec_()