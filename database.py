import mysql.connector
from encryption import Encryption

class Database:
    """
    Represents a database connection handler.
    This class is responsible for establishing a connection to a MySQL database, executing various database operations.
    """

    def __init__(self):
        """
        Initializes the Database class instance by setting up a connection to the MySQL database using credentials
        decrypted from a given URL path.
        """
        self.encryption = Encryption()

        url_path = "secrets/mysql_url"
        with open(url_path, 'r') as file:
            url = self.encryption.decrypt(file.read())

        try:
            self.connection = mysql.connector.connect(
                host=url.split('@')[1].split('/')[0],
                user=url.split('://')[1].split(':')[0],
                password=url.split(':')[2].split('@')[0],
                database=url.split('/')[-1],
                ssl_disabled=False
            )
            self.cursor = self.connection.cursor()  # Tworzenie kursora w konstruktorze
        except mysql.connector.Error as e:
            self.error = "Błąd połączenia z internetem, zrestartuj aplikację."
            raise mysql.connector.Error(f"Error while connecting to database: {e}")

    def __del__(self):
        """
        Destructor that ensures the database connection and cursor are properly closed.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection.is_connected():
            self.connection.close()

    def register(self, first_name, last_name, login, password):
        """
        Registers a new user in the database with the provided first name, last name, login, and password.
        All user data except password is encrypted before being stored. The password is hashed for security.
        :param first_name: (str) The first name of the user.
        :param last_name: (str) The last name of the user.
        :param login: (str) The login identifier for the user.
        :param password: (str) The password for the user.
        """
        first_name = self.encryption.encrypt(first_name)
        last_name = self.encryption.encrypt(last_name)
        login = self.encryption.encrypt(login)
        password = self.encryption.hash(password)

        try:
            self.cursor.execute("INSERT INTO `users` (`firstName`, `lastName`, `login`, `password`) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, login, password))
            self.connection.commit()
        except Exception as e:
            print(e)
            return

    def login_db_check(self, login):
        """
        Checks if a given login exists in the database by decrypting all stored logins
        and comparing them with the provided one.
        :param login: (str) The login identifier to check in the database.
        :return: (boolean) True if the login does not exist in the database, False otherwise.
        """
        try:
            self.cursor.execute("SELECT login FROM users")
        except Exception as e:
            print(e)
            return

        results = self.cursor.fetchall()  # Returns a list of tuples, for example: [("login",),]

        for result in results:
            if self.encryption.decrypt(result[0]) == login:
                return False
        return True

    def login(self, username, password):
        pass

    def clear_users_table(self):
        """
        Deletes all entries from the users table in the database.
        This method is now used when creating a new AES key.
        """
        try:
            self.cursor.execute("DELETE FROM `users`;")
            self.connection.commit()
        except Exception as e:
            print(e)
            return
