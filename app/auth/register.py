from PyQt5.QtCore import Qt

from app.database.database import Database
from app.services.validation import FormValidation
from app.utils.notifications import Notifications


class Register(Notifications):
    """
    A class responsible for user registration processes in the application.
    """
    def __init__(self, app, ui):
        """
        Initializes the Register class with UI elements, sets up user data and error handling structures.
        :param app: The application instance.
        :param ui: The register interface object.
        """
        self.ui = ui
        self.app = app

        self.user_data = {
            "first_name": self.ui.firstNameLabel,
            "last_name": self.ui.lastNameLabel,
            "login": self.ui.loginLabel,
            "password": self.ui.passwordLabel,
            "password2": self.ui.password2Label
        }

        self.error_labels = {
            "first_name": self.ui.firstNameErrorLabel,
            "last_name": self.ui.lastNameErrorLabel,
            "login": self.ui.loginErrorLabel,
            "password": self.ui.passwordErrorLabel,
            "password2": self.ui.password2ErrorLabel
        }

        self.messages = {
            "first_name": "Zła składnia imienia!",
            "last_name": "Zła składnia nazwiska!",
            "login": "",
            "password": "Zła składnia hasła!",
            "password2": "Hasła się różnią!",
            "pass_mark": "✔",
            "prompt_text": "Czy chcesz założyć konto na podane dane?",
            "prompt_title": "Potwierdzenie rejestracji"
        }

        self.duplicate_login_mess = "Login jest już używany!"
        self.login_mess = "Zła składna loginu!"

        self.pass_style_sheet = "color: green; font-size: 20px;"
        self.pass_alignment = Qt.AlignCenter

        self.database = Database()
        self.form_validation = FormValidation()

        self.default_alignment = self.error_labels["login"].alignment()

    def prepare_registration(self):
        """
        Handles the user registration process including form data validation,
        duplicate checks, and user registration in the database.
        """
        form_data = self.form_validation.read_forms(self.user_data)

        if not self.form_validation.fill_check(form_data):
            return

        # False: no error; True: error
        error_states = []

        self.messages["login"] = self.login_mess

        for key in ["first_name", "last_name", "login", "password"]:
            self.clear_formatting(self.error_labels[key], self.default_alignment)
            error_states.append(self.validate_input(form_data, key))

        if True in error_states:
            return

        self.messages["login"] = self.duplicate_login_mess

        for key in ["login", "password2"]:
            self.clear_formatting(self.error_labels[key], self.default_alignment)
            error_states.append(self.validate_credentials(form_data, key))

        if True in error_states:
            return

        if self.question_prompt(self.messages["prompt_text"],
                                self.messages["prompt_title"]):
            self.database.register(self.capitalize_first_letter(form_data["first_name"]),
                                   self.capitalize_first_letter(form_data["last_name"]),
                                   form_data["login"],
                                   form_data["password"])

            self.app.load_login_ui()

    def capitalize_first_letter(self, text):
        """
        Capitalize first letter of given string
        :param text: (str) text to be capitalized
        :return: (str) capitalized text
        """
        return text[0].upper() + text[1:]

    def password_duplication_check(self, password, password2):
        """
        Checks if the two password inputs match.
        :param password: (str) The first password input.
        :param password2: (str) The second password input (confirmation).
        :return: (boolean) True if passwords match, False otherwise.
        """
        return password == password2

    def validate_input(self, form_data, key):
        """
        Validates the input data based on the specified key.
        :param form_data: (dict) The dictionary containing user input data.
        :param key: (str) The dict-key indicating the type of input data to be validated.
        :return: (boolean) True if an error is found, False otherwise.
        """
        error = False

        if key == "first_name" or key == "last_name":
            if not self.form_validation.validate_name(form_data[key]):
                error = True
        elif key == "login":
            if not self.form_validation.validate_login(form_data[key]):
                error = True
        elif key == "password":
            if not self.form_validation.validate_password(form_data[key]):
                error = True

        self.handle_errors(error, key)

        return error

    def validate_credentials(self, form_data, key):
        """
        Validates login duplicate in database and both password labels matching rules.
        :param form_data: (dict) The dictionary containing user input data.
        :param key: (str) The dict-key indicating login or password.
        :return: (boolean) True if an error is found, False otherwise.
        """
        error = False
        if key == "login":
            # if login exists in database
            if not self.database.login_db_check(form_data[key]):
                # mark error
                error = True

        elif key == "password2":
            # if passwords does not match
            if not self.password_duplication_check(form_data["password"], form_data["password2"]):
                error = True

        self.handle_errors(error, key)

        return error

    def handle_errors(self, error, key):
        """
        Handles the display of errors or success messages based on the validation results.
        :param error: (boolean) True if an error is found, False otherwise.
        :param key: (str) The dict-key indicating the type of input data.
        """
        if error:
            self.error_labels[key].setText(self.messages[key])
        else:
            self.update_label(self.error_labels[key], self.pass_style_sheet, self.messages["pass_mark"],
                              self.pass_alignment)

    def show_info(self):
        """
        Displays information about the input data syntax policy.
        """
        info = ("• Imię i Nazwisko może się składać tylko z liter lub znaku '-',\n"
                "• Login musi mieć od 6 do 30 znaków oraz może zawierać litery lub cyfry,\n"
                "• Hasło musi mieć od 6 do 30 znaków oraz może zawierać litery, cyfry lub znaki specjalne.")

        self.information_prompt(info, "Polityka składni.")
