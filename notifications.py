from PyQt5.QtWidgets import QMessageBox


class Notifications:
    """Klasa do zarządzania powiadomieniami i monitami w aplikacji."""

    def __init__(self, style_sheet, alignment):
        self.style_sheet = style_sheet
        self.alignment = alignment

    def confirmation_prompt(self, text, title):
        """Wyświetla okno dialogowe z prośbą o potwierdzenie akcji."""
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(text)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        if msg_box.exec() == QMessageBox.Yes:
            return True
        return False

    def set_style_sheet(self, label, style_sheet=None):
        """Ustawia arkusz stylów dla danego elementu interfejsu."""
        if style_sheet is None:
            style_sheet = self.style_sheet
        label.setStyleSheet(style_sheet)

    def set_alignment(self, label, alignment=None):
        """Ustawia wyrównanie dla danego elementu interfejsu."""
        if alignment is None:
            alignment = self.alignment
        label.setAlignment(alignment)

    def set_notification(self, label, text=""):
        """Ustawia tekst powiadomienia dla danego elementu interfejsu."""
        label.setText(text)
