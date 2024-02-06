import mysql.connector


class Database:
    """Klasa odpowiadająca za połączenie z bazą danych MySQL i operacje na danych użytkowników."""

    def __init__(self):
        """Inicjalizuje połączenie z bazą danych."""
        self.url = "mysql://sql11682263:LVhJMjsENR@sql11.freesqldatabase.com/sql11682263"
        try:
            self.connection = mysql.connector.connect(
                host=self.url.split('@')[1].split('/')[0],
                user=self.url.split('://')[1].split(':')[0],
                password=self.url.split(':')[2].split('@')[0],
                database=self.url.split('/')[-1]
            )
        except mysql.connector.Error:
            self.error = "Błąd połączenia z internetem, zrestartuj aplikację."

    def __del__(self):
        """Zamyka połączenie z bazą danych przy usuwaniu instancji klasy."""
        if self.connection.is_connected():
            self.connection.close()

    def register(self, first_name, last_name, login, password):
        """Rejestruje nowego użytkownika w bazie danych."""
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO `users` (`firstName`, `lastName`, `login`, `password`) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, login, password)
        )
        self.connection.commit()

    def login_db_check(self, login):
        """Sprawdza, czy podany login już istnieje w bazie danych."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT login FROM users")
        results = cursor.fetchall()  # Zwraca listę krotek, np. [("login",),]

        for result in results:
            if result[0] == login:
                return False
        return True

    def login(self, username, password):
        """Miejsce na implementację logowania."""
        pass

    def hash(self, password):
        """Miejsce na implementację hashowania haseł."""
        pass

    def encrypt(self):
        """Miejsce na implementację szyfrowania."""
        pass

    def decrypt(self):
        """Miejsce na implementację deszyfrowania."""
        pass
