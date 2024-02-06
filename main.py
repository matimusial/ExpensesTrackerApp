from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys
import database, register
import UI.login.sources.login_rc
import UI.register.sources.register_rc

'''
Main class, when the program starts.
Each function has only button operations.
'''

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.database = database.Database()
        self.loadLoginUI()
        self.show()

    def loadLoginUI(self):
        uic.loadUi("UI/login/login.ui", self)
        if hasattr(self.database, 'error'): self.errorLabel.setText(self.database.error)
        self.registerButton.clicked.connect(self.loadRegisterUI)

    def loadRegisterUI(self):
        ui = uic.loadUi("UI/register/register.ui", self)
        self.register = register.Register(ui)
        self.backButton.clicked.connect(self.loadLoginUI)
        self.registerButton.clicked.connect(self.register.prepareRegistration)

app = QApplication(sys.argv)
window = App()
app.exec_()