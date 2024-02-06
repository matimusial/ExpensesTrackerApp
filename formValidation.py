
class FormValidation:

    """
    A class for form validation.
    """

    def __init__(self):
        pass

    def read_forms(self, user_data):

        form_data = {}
        for key, label in user_data.items():
            form_data[key] = label.text()  # Read values from labels to dict, for example: firstName: "Mateusz"
        return form_data

    def fill_check(self, data):
        for value in data.values():
            if value == "":
                return False
        return True

    def login_check(self, login):
        pass

    def password_check(self, password):
        pass

    def name_check(self, name):
        pass