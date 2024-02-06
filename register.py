from PyQt5.QtCore import Qt

from database import Database
from formValidation import FormValidation
from notifications import Notifications


class Register:

    """
    A class responsible for user registration.
    """

    def __init__(self, ui):
        self.ui = ui


        self.user_data = {
            "first_name": self.ui.firstNameLabel,
            "last_name": self.ui.lastNameLabel,
            "login": self.ui.loginLabel,
            "password": self.ui.passwordLabel,
            "password2": self.ui.password2Label,
        }

        self.duplicate_labels = {
            "password": self.ui.passwordDuplicateLabel,
            "login": self.ui.loginDuplicateLabel,
        }

        self.error_messages = {
            "password": "Hasła się różnią!",
            "login": "Login jest już używany!"
        }

        style_sheet = self.ui.centralwidget.styleSheet()
        default_alignment = self.duplicate_labels["login"].alignment()

        self.pass_mark = "✔"
        self.pass_style_sheet = "color: green; font-size: 20px;"
        self.pass_alignment = Qt.AlignCenter

        self.database = Database()
        self.form_validation = FormValidation()
        self.notifications = Notifications(style_sheet, default_alignment)

    def registration(self):

        form_data = self.form_validation.read_forms(self.user_data)

        for label in self.duplicate_labels.values():
            self.notifications.set_style_sheet(label, "")
            self.notifications.set_alignment(label)

        if not self.form_validation.fill_check(form_data):
            return

        error = []   # False: no error; True: error

        for key, value in self.error_messages.items():
            error.append(self.login_and_password_check(form_data, key))

        if True in error: return

        if not self.notifications.confirmation_prompt("Czy chcesz założyć konto na podane dane?", "Potwierdzenie rejestracji"):
            return

        self.database.register(form_data["first_name"], form_data["last_name"], form_data["login"], form_data["password"])

    def update_label(self, label, style_sheet, notification, alignment):
        self.notifications.set_style_sheet(label, style_sheet)
        self.notifications.set_notification(label, notification)
        self.notifications.set_alignment(label, alignment)

    def password_duplication_check(self, password, password2):
        return password == password2

    def login_and_password_check(self, form_data, key):
        error = False

        if key == "login":
            if not self.database.login_db_check(form_data[key]):
                error = True
        elif key == "password":
            if not self.password_duplication_check(form_data["password"], form_data["password2"]):
                error = True

        if not error:
            self.update_label(self.duplicate_labels[key], self.pass_style_sheet, self.pass_mark, self.pass_alignment)
        else:
            self.notifications.set_notification(self.duplicate_labels[key], self.error_messages[key])

        return error