from PyQt5.QtWidgets import QMessageBox
import database


class Register:
    def __init__(self, ui):
        self.ui = ui
        self.database = database.Database()

        self.user_data = {
            "firstName": self.ui.firstNameLabel,
            "lastName": self.ui.lastNameLabel,
            "login": self.ui.loginLabel,
            "password": self.ui.passwordLabel,
            "password2": self.ui.password2Label,
        }

    def prepareRegistration(self):

        form_data = {}
        for key, label in self.user_data.items():
            form_data[key] = label.text()   # reads a values form labels to a dict eg. firstName: "mateusz" etc

        if self.fillCheck(form_data) == False: return

        if form_data["password"] != form_data["password2"]:
            self.ui.passwordDuplicateLabel.setText("Hasła się różnią!")
            return

        if self.database.checkLogin(form_data["login"]) == False:
            self.ui.loginDuplicateLabel.setText("Login jest już używany")
            return

        if self.confirmationPrompt() == False: return

        #hash()
        self.database.register(form_data["firstName"], form_data["lastName"], form_data["login"], form_data["password"])


    def confirmationPrompt(self):

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Czy chcesz założyć konto na podane dane?")
        msgBox.setWindowTitle("Potwierdzenie rejestracji")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnValue = msgBox.exec()

        if returnValue == QMessageBox.Yes:
            return True
        else:
            return False

    def fillCheck(self, data):
        for value in data.values():
            if value == "": return False
        return True