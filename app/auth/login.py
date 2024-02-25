from app.database.database import Database
from app.services.validation import FormValidation
from app.utils.notifications import Notifications


class Login(Notifications):
    """
    The Login class handles user authentication within the application.
    This class is responsible for managing the login process, including
    form validation, interaction with the database for authentication,
    and displaying relevant notifications to the user.
    """

    def __init__(self, app, ui):
        """
        Initialize the Login class.

        Parameters:
        :param app: The application instance.
        :param ui: (QT constant) The user interface instance.
        """
        self.app = app
        self.ui = ui
        self.database = Database()

        self.user_data = {
            "login": self.ui.loginLabel,
            "password": self.ui.passwordLabel
        }

        self.errorLabel = self.ui.errorLabel

        self.form_validation = FormValidation()

    def login(self):
        """
        Perform user login based on form data.
        Reads form data, performs validation, and attempts login (loads menu ui).
        Displays appropriate notifications.
        """
        error_message = "Błędny login lub hasło!"

        form_data = self.form_validation.read_forms(self.user_data)

        if not self.form_validation.fill_check(form_data):
            return

        result = self.database.login(form_data["login"], form_data["password"])

        if result[0]:
            self.app.load_menu_ui(result[1])
        else:
            self.errorLabel.setText(error_message)
