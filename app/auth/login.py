from app.database.database import Database
from app.services.validation import FormValidation


class Login:
    def __init__(self, ui):
        self.ui = ui
        self.database = Database()

        self.user_data = {
            "login": self.ui.loginLabel,
            "password": self.ui.passwordLabel
        }

        self.form_validation = FormValidation()

    def login(self):

        form_data = self.form_validation.read_forms(self.user_data)

        if not self.form_validation.fill_check(form_data):
            return

        if self.database.login_db_check(form_data["login"]):
            print("Login nie istnieje")
            return
