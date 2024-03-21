import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import QDate

from app.database.database import Database
from app.auth.register import Register
from app.auth.login import Login


class App(QMainWindow):
    """
    The main application window class.
    Initializes the application with the login window.
    """
    def __init__(self):
        """
        Initializes the application window, establishes a database connection, and loads the login interface.
        """
        super().__init__()
        self.database = Database()
        self.load_expense_ui(57)
        #self.load_login_ui()
        self.show()

    def load_login_ui(self):
        """
        Loads the login interface and sets up connections for login and register buttons.
        """
        import app.ui.login.sources.login_rc
        ui_path = "app/ui/login/login.ui"
        ui = uic.loadUi(ui_path, self)
        self.login = Login(self, ui)
        if hasattr(self.database, 'error'):
            self.errorLabel.setText(self.database.error)
        self.registerButton.clicked.connect(self.load_register_ui)
        self.loginButton.clicked.connect(self.login.login)

    def load_register_ui(self):
        """
        Loads the registration interface and sets up connections for the registration, info, and back buttons.
        """
        import app.ui.register.sources.register_rc
        ui_path = "app/ui/register/register.ui"
        ui = uic.loadUi(ui_path, self)
        self.register = Register(self, ui)
        self.backButton.clicked.connect(self.load_login_ui)
        self.registerButton.clicked.connect(self.register.prepare_registration)
        self.infoButton.clicked.connect(self.register.show_info)

    def load_menu_ui(self, id):
        """
        Loads the menu interface and sets up connections for logout, income addition, and expense.
        :param id: (int) User's id in database.
        """
        import app.ui.menu.sources.menu_rc
        ui_path = "app/ui/menu/menu.ui"
        uic.loadUi(ui_path, self)
        name = self.database.search_from_users("firstname", id)
        self.welcomeButton.setText(f"Witaj {name}!")
        self.logoutButton.clicked.connect(self.load_login_ui)
        #self.analysisButton.clicked.connect(self)
        #self.incomeButton.clicked.connect(self)
        self.expenseButton.clicked.connect(lambda: self.load_expense_ui(id))

    def load_expense_ui(self, id):
        """
        Loads the expense interface and sets up connections for logout and data entry.
        :param id: (int) User's id in database.
        """
        import app.ui.expense.sources.expense_rc
        ui_path = "app/ui/expense/expense.ui"
        uic.loadUi(ui_path, self)

        current_date = QDate.currentDate()
        self.dateLabel.setText(current_date.toString("dd-MM-yyyy"))

        double_validator = QDoubleValidator()
        self.amountLabel.setValidator(double_validator)

        self.backButton.setVisible(False)
        self.logoutButton.clicked.connect(self.load_login_ui)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
