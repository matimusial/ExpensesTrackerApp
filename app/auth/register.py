from PyQt5.QtCore import Qt

from app.database.database import Database
from app.services.validation import FormValidation
from app.utils.notifications import Notifications


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
            "firstname": self.ui.firstNameLabel,
            "lastname": self.ui.lastNameLabel,
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

        self.notifications = Notifications(style_sheet, default_alignment, self.ui)

    def prepare_registration(self):
        """
        Handles the user registration process including form data validation,
        duplicate checks, and user registration in the database.
        """
        form_data = self.form_validation.read_forms(self.user_data)

        for label in self.error_labels.values():
            self.notifications.clear_formatting(label)

        if not self.form_validation.fill_check(form_data):
            return

        # self.form_validation.name_check(form_data["firstname"], form_data["lastname"])
        # self.form_validation.validate_login(form_data["login"])
        # self.form_validation.validate_password(form_data["password"])
        # "✖"

        error_states = []  # False: no error; True: error

        for key, value in self.error_messages.items():
            error_states.append(self.check_errors(form_data, key))

        if True in error_states:
            return

        prompt_text = "Czy chcesz założyć konto na podane dane?"
        prompt_title = "Potwierdzenie rejestracji"

        if self.notifications.question_prompt(prompt_text, prompt_title):
            self.database.register(form_data["firstname"], form_data["lastname"],
                                   form_data["login"], form_data["password"])

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
        Validates login duplicate in database and both password labels matching rules.
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
            self.notifications.update_label(self.error_labels[key], pass_style_sheet, pass_mark, pass_alignment)

        return error
