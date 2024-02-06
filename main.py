import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

from database import Database
from register import Register

# Importowanie zasobów z UI
import UI.login.sources.login_rc
import UI.register.sources.register_rc


class App(QMainWindow):
    """Główna klasa aplikacji uruchamianej przy starcie.

    Każda funkcja w tej klasie obsługuje operacje związane z przyciskami.
    """

    def __init__(self):
        super().__init__()
        self.database = Database()
        self.load_login_ui()
        self.show()

    def load_login_ui(self):
        """Ładuje interfejs użytkownika dla ekranu logowania."""
        uic.loadUi("UI/login/login.ui", self)
        if hasattr(self.database, 'error'):
            self.errorLabel.setText(self.database.error)
        self.registerButton.clicked.connect(self.load_register_ui)

    def load_register_ui(self):
        """Ładuje interfejs użytkownika dla ekranu rejestracji."""
        ui = uic.loadUi("UI/register/register.ui", self)
        self.register = Register(ui)
        self.backButton.clicked.connect(self.load_login_ui)
        self.registerButton.clicked.connect(self.register.registration)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
