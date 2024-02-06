from PyQt5.QtCore import Qt

import formValidation
from database import Database
from formValidation import FormValidation
from notifications import Notifications


class Register:
    def __init__(self, ui):
        self.ui = ui

        self.user_data = {
            "firstName": self.ui.firstNameLabel,
            "lastName": self.ui.lastNameLabel,
            "login": self.ui.loginLabel,
            "password": self.ui.passwordLabel,
            "password2": self.ui.password2Label,
        }

        styleSheet = self.ui.centralwidget.styleSheet()
        defaultAlignment = Qt.AlignLeft

        self.passwordError = "Hasła się różnią!"
        self.Pass = "✔"
        self.PassStyleSheet = "color: green;font-size: 20px;"
        self.loginError = "Login jest już używany!"
        self.PassAlignment = Qt.AlignCenter

        self.database = Database()
        self.formValidation = FormValidation()
        self.notifications = Notifications(styleSheet, defaultAlignment)

    def Registration(self):

        form_data = self.formValidation.readForms(self.user_data)

        if self.formValidation.fillCheck(form_data) == False: return

        self.notifications.setStyleSheet(self.ui.centralwidget)
        self.notifications.setAlignment(self.ui.passwordDuplicateLabel)
        self.notifications.setAlignment(self.ui.loginDuplicateLabel)

        error = True  # False - error, True no errors

        if self.formValidation.passwordCheck(form_data["password"], form_data["password2"]) == False:
            error = False
            self.notifications.setNotification(self.ui.passwordDuplicateLabel, self.passwordError)
        else:
            self.notifications.setStyleSheet(self.ui.passwordDuplicateLabel, self.PassStyleSheet)
            self.notifications.setNotification(self.ui.passwordDuplicateLabel, self.Pass)
            self.notifications.setAlignment(self.ui.passwordDuplicateLabel, self.PassAlignment)

        if self.database.loginDBCheck(form_data["login"]) == False:
            error = False
            self.notifications.setNotification(self.ui.loginDuplicateLabel, self.loginError)
        else:
            self.notifications.setStyleSheet(self.ui.loginDuplicateLabel, self.PassStyleSheet)
            self.notifications.setNotification(self.ui.loginDuplicateLabel, self.Pass)
            self.notifications.setAlignment(self.ui.loginDuplicateLabel, self.PassAlignment)

        if error == False: return


        if self.notifications.confirmationPrompt("Czy chcesz założyć konto na podane dane?","Potwierdzenie rejestracji") == False: return

        self.database.register(form_data["firstName"], form_data["lastName"], form_data["login"], form_data["password"])