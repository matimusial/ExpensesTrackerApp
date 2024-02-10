
class FormValidation:
    """
    A class dedicated validate form inputs in an application.
    """

    def __init__(self):
        """
        Initializes the FormValidation class.
        """
        pass

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
        :return: True if all fields are filled, False otherwise.
        """
        for value in data.values():
            if value == "":
                return False
        return True

    def login_check(self, login):

        if len(login)>6 or len(login)>30:
            raise ValueError("Login powinien mieć od 6 do 30 znaków.")
        return True

    def word_check(self, word):
        pass

    def password_check(self, password):
        pass

    def name_check(self, firstname, lastname):
        pass
