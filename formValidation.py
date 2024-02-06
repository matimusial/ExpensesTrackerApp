from PyQt5.QtCore import Qt

class FormValidation:
    def __init__(self):
        pass

    def readForms(self, user_data):
        form_data = {}
        for key, label in user_data.items():
            form_data[key] = label.text()  # reads a values form labels to a dict eg. firstName: "mateusz" etc
        return form_data

    def fillCheck(self, data):
        for value in data.values():
            if value == "": return False
        return True

    def loginCheck(self, login):

        pass

    def passwordCheck(self, password, password2):
        if password != password2: return True

    def nameCheck(self, name):
        pass