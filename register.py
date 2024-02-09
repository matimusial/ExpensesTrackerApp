from PyQt5.QtCore import Qt

from database import Database
from formValidation import FormValidation
from notifications import Notifications


class Register:
    """
    A class responsible for user registration processes in the application.
    """

    def __init__(self, ui):
        """
        Initializes the Register class with UI elements, sets up user data and error handling structures.
        :param ui: The register interface object.
        """
        self.ui = ui

        self.user_data = {
            "first_name": self.ui.firstNameLabel,
            "last_name": self.ui.lastNameLabel,
            "login": self.ui.loginLabel,
            "password": self.ui.passwordLabel,
            "password2": self.ui.password2Label
        }

        self.error_labels = {
            "password": self.ui.passwordErrorLabel,
            "login": self.ui.loginErrorLabel
        }

        self.error_messages = {
            "password": "Hasła się różnią!",
            "login": "Login jest już używany!"
        }

        self.database = Database()
        self.form_validation = FormValidation()

        style_sheet = self.ui.centralwidget.styleSheet()
        default_alignment = self.error_labels["login"].alignment()

        self.notifications = Notifications(style_sheet, default_alignment)

    def prepare_registration(self):
        """
        Handles the user registration process including form data validation,
        duplicate checks, and user registration in the database.
        """
        form_data = self.form_validation.read_forms(self.user_data)

        for label in self.error_labels.values():  # resets the stylesheet in error labels
            self.notifications.set_style_sheet(label, "")
            self.notifications.set_alignment(label)

        if not self.form_validation.fill_check(form_data):
            return

        error_states = []  # False: no error; True: error

        for key, value in self.error_messages.items():  # checks both conditions for registration
            error_states.append(self.check_errors(form_data, key))

        if True in error_states: return

        prompt_text = "Czy chcesz założyć konto na podane dane?"
        prompt_title = "Potwierdzenie rejestracji"

        if self.notifications.confirmation_prompt(prompt_text, prompt_title):
            self.database.register(form_data["first_name"], form_data["last_name"],
                                   form_data["login"], form_data["password"])

    def update_label(self, label, style_sheet, notification, alignment):
        """
        Updates a label with specified styles and notification text.
        :param label: (QLabel class) The label to be updated.
        :param style_sheet: (str) The CSS style sheet to apply to the label.
        :param notification: (str) The notification text to display on the label.
        :param alignment: (Qt constant) The alignment for the notification text.
        """
        self.notifications.set_style_sheet(label, style_sheet)
        self.notifications.set_notification(label, notification)
        self.notifications.set_alignment(label, alignment)

    def password_duplication_check(self, password, password2):
        """
        Checks if the two password inputs match.
        :param password: (str) The first password input.
        :param password2: (str) The second password input (confirmation).
        :return: (boolean) True if passwords match, False otherwise.
        """
        return password == password2

    def check_errors(self, form_data, key):
        """
        Validates login duplicate in database and password matching rules.
        :param form_data: (dict) The dictionary containing user input data.
        :param key: (str) The dict-key indicating login or password.
        :return: (boolean) True if an error is found, False otherwise.
        """
        error = False
        pass_mark = "✔"
        pass_style_sheet = "color: green; font-size: 20px;"
        pass_alignment = Qt.AlignCenter

        if key == "login":
            if not self.database.login_db_check(form_data[key]):
                error = True
        elif key == "password":
            if not self.password_duplication_check(form_data["password"], form_data["password2"]):
                error = True

        if error:
            self.notifications.set_notification(self.error_labels[key], self.error_messages[key])
        else:
            self.update_label(self.error_labels[key], pass_style_sheet, pass_mark, pass_alignment)

        return error
