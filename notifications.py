from PyQt5.QtWidgets import QMessageBox

class Notifications:
    def __init__(self, styleSheet, alignment):
        self.styleSheet = styleSheet
        self.alignment = alignment


    def confirmationPrompt(self, text, title):

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        if msgBox.exec() == QMessageBox.Yes:
            return True
        return False

    def setStyleSheet(self, label, styleSheet = None):
        if styleSheet is None:
            styleSheet = self.styleSheet
        label.setStyleSheet(styleSheet)

    def setAlignment(self, label, alignment = None):
        if alignment is None:
            alignment = self.alignment
        label.setAlignment(alignment)

    def setNotification(self, label, text = ""):
        label.setText(text)