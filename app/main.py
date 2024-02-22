import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

from app.database.database import Database
from app.auth.register import Register
from app.auth.login import Login

import app.ui.login.sources.login_rc
import app.ui.register.sources.register_rc
import app.ui.menu.sources.menu_rc


class App(QMainWindow):
    """
    The main application window class.
    It initializes the application with login window.
    """

    def __init__(self):
        """
        Initializes the application window, the database connection, and loads the login interface.
        """
        super().__init__()
        self.database = Database()
        self.load_login_ui()
        self.show()

    def load_login_ui(self):
        """
        Loads the login interface and sets up connections for login and register buttons.
        """
        ui_path = "app/ui/login/login.ui"
        ui = uic.loadUi(ui_path, self)
        self.login = Login(self, ui)
        if hasattr(self.database, 'error'):
            self.errorLabel.setText(self.database.error)
        self.registerButton.clicked.connect(self.load_register_ui)
        self.loginButton.clicked.connect(self.login.login)

    def load_register_ui(self):
        """
        Loads the registration interface and sets up connections for the registration, info and back buttons.
        """
        ui_path = "app/ui/register/register.ui"
        ui = uic.loadUi(ui_path, self)
        self.register = Register(self, ui)
        self.backButton.clicked.connect(self.load_login_ui)
        self.registerButton.clicked.connect(self.register.prepare_registration)
        self.infoButton.clicked.connect(self.register.show_info)

    def load_menu_ui(self, name):
        """
        Loads the menu interface and sets up connections for the logout, income add and expanse.
        :param name: (str) User's name.
        """
        ui_path = "app/ui/menu/menu.ui"
        uic.loadUi(ui_path, self)
        self.welcomeButton.setEnabled(False)
        self.welcomeButton.setText(f"Witaj {name}!")
        self.logoutButton.clicked.connect(self.load_login_ui)
        #self.analysisButton.clicked.connect(self)
        #self.incomeButton.clicked.connect(self)
        #self.expenseButton.clicked.connect(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
