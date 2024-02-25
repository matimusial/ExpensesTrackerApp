from PyQt5.QtWidgets import QMessageBox


class Notifications:
    """
    A class for managing notifications and alerts within an application.
    Provides methods to display confirmation prompts, set styles, and alignments for labels.
    """
    def question_prompt(self, text, title="Confirmation"):
        """
        Displays a modal question dialog with specified text and title, providing Yes and No options.
        :param text: (str) Text to display in the question prompt.
        :param title: (str) Title of the question prompt window.
        :return: (boolean) True if the user clicks 'Yes', False otherwise.
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText(text)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return msg_box.exec() == QMessageBox.Yes

    def information_prompt(self, text, title="Information"):
        """
        Displays a modal information dialog with specified text and title, providing Ok options.
        :param text: (str) Text to display in the information prompt.
        :param title: (str) Title of the information prompt window.
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(text)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def clear_formatting(self, label, alignment="", style_sheet=""):
        """
        Clears the formatting (style sheet and alignment) for a dictionary of labels.
        :param label: (QLabel class) The label to clear formatting for.
        :param alignment: (Qt constant) The alignment for the label text.
        :param style_sheet: (str) The CSS style sheet to apply to the label.
        """
        label.setAlignment(alignment)
        label.setStyleSheet(style_sheet)

    def update_label(self, label, style_sheet, notification, alignment):
        """
        Updates a label with specified styles and notification text.
        :param label: (QLabel class) The label to be updated.
        :param style_sheet: (str) The CSS style sheet to apply to the label.
        :param notification: (str) The notification text to display on the label.
        :param alignment: (Qt constant) The alignment for the label text.
        """
        label.setStyleSheet(style_sheet)
        label.setText(notification)
        label.setAlignment(alignment)
