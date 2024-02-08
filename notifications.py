from PyQt5.QtWidgets import QMessageBox


class Notifications:

    """
    A class for managing notifications and alerts in the application.
    """

    def __init__(self, style_sheet="", alignment=""):
        self.style_sheet = style_sheet
        self.alignment = alignment

    def confirmation_prompt(self, text, title="Confirmation"):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(text)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        return msg_box.exec() == QMessageBox.Yes

    def set_style_sheet(self, label, style_sheet=None):
        if style_sheet is None:
            style_sheet = self.style_sheet
        label.setStyleSheet(style_sheet)

    def set_alignment(self, label, alignment=None):
        if alignment is None:
            alignment = self.alignment
        label.setAlignment(alignment)

    def set_notification(self, label, text=""):
        label.setText(text)