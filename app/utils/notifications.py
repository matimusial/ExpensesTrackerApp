from PyQt5.QtWidgets import QMessageBox


class Notifications:
    """
    A class for managing notifications and alerts within an application.
    Provides methods to display confirmation prompts, set styles and alignments for labels.
    """

    def __init__(self, style_sheet="", alignment="", ui=""):
        """
        Initializes the Notifications class with style sheet and alignment.
        Ensures that UI is loaded before initialization.
        :param style_sheet: (str) CSS default style sheet of current UI.
        :param alignment: (Qt constant) The default alignment for the notification text.
        :param ui: (QT constant) Current UI.
        :raises ValueError: If "ui" parameter is empty.
        """
        if ui == "":
            raise ValueError("UI is not loaded.")
        self.style_sheet = style_sheet
        self.alignment = alignment

    def question_prompt(self, text, title="Confirmation"):
        """
        Displays a modal question dialog with specified text and title, providing Yes and No options.
        :param text: (str) Text to display in the question prompt.
        :param title: (str) Title of the question prompt window.
        :return: (boolean) True if user clicks 'Yes', False otherwise.
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

    def set_style_sheet(self, label, style_sheet=None):
        """
        Applies a CSS style sheet to a given label. Uses default UI style sheet if none provided.
        :param label: (QLabel class) The label to apply the style sheet to.
        :param style_sheet: (str) CSS style sheet to apply.
        """
        if style_sheet is None:
            style_sheet = self.style_sheet
        label.setStyleSheet(style_sheet)

    def set_alignment(self, label, alignment=None):
        """
        Sets the alignment for a given label. Uses default class alignment if none provided.
        :param label: (QLabel class) The label to apply the alignment to.
        :param alignment: (QT constant) Alignment to apply.
        """
        if alignment is None:
            alignment = self.alignment
        label.setAlignment(alignment)

    def set_notification(self, label, text=""):
        """
        Sets the text for a given label to display a notification.
        :param label: (QLabel class) The label to set the notification text on.
        :param text: (str) Text to display as the notification.
        """
        label.setText(text)

    def clear_formatting(self, label):
        """
        Clears the formatting (style sheet and alignment) for a dictionary of labels.
        :param label: (QLabel class) The label to clear formatting for.
        """
        self.set_style_sheet(label, "")
        self.set_alignment(label)

    def update_label(self, label, style_sheet, notification, alignment):
        """
        Updates a label with specified styles and notification text.
        :param label: (QLabel class) The label to be updated.
        :param style_sheet: (str) The CSS style sheet to apply to the label.
        :param notification: (str) The notification text to display on the label.
        :param alignment: (Qt constant) The alignment for the notification text.
        """
        self.set_style_sheet(label, style_sheet)
        self.set_notification(label, notification)
        self.set_alignment(label, alignment)
