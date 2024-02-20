import string


class FormValidation:
    """
    A class dedicated validate form inputs in an application.
    """

    def __init__(self):
        """
        Initializes the FormValidation class with rises_errors dictionary.
        """
        self.raises_errors = {
            "lastname_content": "Nazwisko powinno zawierać tylko litery (en).",
            "firstname_content": "Imię powinno zawierać tylko litery (en).",

            "password_content": "Hasło powinno zawierać litery (en), cyfry oraz znaki specjalne.",
            "login_content": "Login powinien zawierać tylko litery (en) lub cyfry.",

            "password_len": "Hasło powinno mieć od 6 do 30 znaków.",
            "login_len": "Login powinien mieć od 6 do 30 znaków."
        }

    def read_forms(self, user_data):
        """
        Read values from labels to dict.
        :param user_data: (dict) Labels of UI. {labelName: QLabel class}
        :return: (dict) Text included in labels. {first_name: "Mateusz"}
        """
        form_data = {}
        for key, label in user_data.items():
            form_data[key] = label.text()
        return form_data

    def fill_check(self, data):
        """
        Checks if all form fields are filled.
        :param data: (dict) Text included in labels. {first_name: "Mateusz"}
        :return: (boolean) True if all fields are filled, False otherwise.
        """
        for value in data.values():
            if value == "":
                return False
        return True

    def validate_login(self, login):
        """
        Validates if login length is between 6 and 30 and if consists of letters or digits.
        :param login: (str) login to validate.
        :return: (boolean) False if login does not meet the validation criteria, True otherwise.
        """
        if len(login) < 6 or len(login) > 30:
            return False

        charset = set(string.ascii_letters + string.digits)

        for i in login:
            if i not in charset:
                return False

        return True

    def validate_password(self, password):
        """
        Validates if password length is between 6 and 30 and if consists of letters, digits and special characters.
        :param password: (str) password to validate.
        :return: (boolean) False if password does not meet the validation criteria, True otherwise.
        """
        if len(password) < 6 or len(password) > 30:
            return False

        charset = set(string.ascii_letters + string.digits + string.punctuation)

        for i in password:
            if i not in charset:
                return False

        return True

    def name_check(self, firstname, lastname):
        """
        Validates if firstname and lastname consist only of letters.
        :param firstname: (str) first name to validate.
        :param lastname: (str) last name to validate.
        :return: (boolean) False if firstname or lastname does not meet the validation criteria, True otherwise.
        """
        charset = set(string.ascii_letters)

        for i in firstname:
            if i not in charset:
                return False

        for i in lastname:
            if i not in charset:
                return False

        return True
