
class FormValidation:
    """Klasa do walidacji formularzy."""

    def __init__(self):
        pass

    def read_forms(self, user_data):
        """Czyta dane z formularzy i zapisuje je w słowniku."""
        form_data = {}
        for key, label in user_data.items():
            form_data[key] = label.text()  # Przeczytane wartości z etykiet, np. firstName: "Mateusz"
        return form_data

    def fill_check(self, data):
        """Sprawdza, czy wszystkie pola formularza zostały wypełnione."""
        for value in data.values():
            if value == "":
                return False
        return True

    def login_check(self, login):
        """Miejsce na implementację walidacji loginu."""
        pass

    def password_check(self, password):
        """Miejsce na implementację walidacji hasła."""
        pass

    def name_check(self, name):
        """Miejsce na implementację walidacji imienia."""
        pass
