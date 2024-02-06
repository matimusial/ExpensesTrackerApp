from PyQt5.QtCore import Qt

from database import Database
from formValidation import FormValidation
from notifications import Notifications


class Register:
    """Klasa odpowiadająca za rejestrację użytkowników."""

    def __init__(self, ui):
        self.ui = ui

        # Dane użytkownika pobierane z formularza
        self.user_data = {
            "first_name": self.ui.firstNameLabel,
            "last_name": self.ui.lastNameLabel,
            "login": self.ui.loginLabel,
            "password": self.ui.passwordLabel,
            "password2": self.ui.password2Label,
        }

        # Etykiety informujące o błędach
        self.duplicate_labels = {
            "password": self.ui.passwordDuplicateLabel,
            "login": self.ui.loginDuplicateLabel,
        }

        style_sheet = self.ui.centralwidget.styleSheet()
        default_alignment = self.duplicate_labels["login"].alignment()

        self.password_error = "Hasła się różnią!"
        self.pass_mark = "✔"
        self.pass_style_sheet = "color: green; font-size: 20px;"
        self.login_error = "Login jest już używany!"
        self.pass_alignment = Qt.AlignCenter

        self.database = Database()
        self.form_validation = FormValidation()
        self.notifications = Notifications(style_sheet, default_alignment)

    def registration(self):
        """Obsługuje proces rejestracji nowego użytkownika."""
        form_data = self.form_validation.read_forms(self.user_data)

        for label in self.duplicate_labels.values():
            self.notifications.set_style_sheet(label, "")
            self.notifications.set_alignment(label)

        if not self.form_validation.fill_check(form_data):
            return

        error = True  # Zakładamy, że nie ma błędów

        if not self.password_duplication_check(form_data["password"], form_data["password2"]):
            error = False
            self.notifications.set_notification(self.duplicate_labels["password"], self.password_error)
        else:
            self.update_label(self.duplicate_labels["password"], self.pass_style_sheet, self.pass_mark, self.pass_alignment)

        if not self.database.login_db_check(form_data["login"]):
            error = False
            self.notifications.set_notification(self.duplicate_labels["login"], self.login_error)
        else:
            self.update_label(self.duplicate_labels["login"], self.pass_style_sheet, self.pass_mark, self.pass_alignment)

        if not error:
            return

        if not self.notifications.confirmation_prompt("Czy chcesz założyć konto na podane dane?", "Potwierdzenie rejestracji"):
            return

        self.database.register(form_data["first_name"], form_data["last_name"], form_data["login"], form_data["password"])

    def update_label(self, label, style_sheet, notification, alignment):
        """Aktualizuje etykietę zgodnie z podanymi parametrami."""
        self.notifications.set_style_sheet(label, style_sheet)
        self.notifications.set_notification(label, notification)
        self.notifications.set_alignment(label, alignment)

    def password_duplication_check(self, password, password2):
        """Sprawdza, czy hasła się zgadzają."""
        return password == password2
