import mysql.connector
from encryption import Encryption

class Database:

    """
    A class responsible for connecting to a MySQL database and performing operations on user data.
    """

    def __init__(self):

        self.encryption = Encryption()
        url_path = "secrets/mysql_url"

        with open(url_path, 'r') as file:
            self.url = file.read()
        self.url = self.encryption.decrypt(self.url)

        try:
            self.connection = mysql.connector.connect(
                host=self.url.split('@')[1].split('/')[0],
                user=self.url.split('://')[1].split(':')[0],
                password=self.url.split(':')[2].split('@')[0],
                database=self.url.split('/')[-1],
                ssl_disabled = False
            )
        except mysql.connector.Error:
            self.error = "Błąd połączenia z internetem, zrestartuj aplikację."


    def __del__(self):
        if self.connection.is_connected():
            self.connection.close()

    def register(self, first_name, last_name, login, password):

        try:
            first_name = self.encryption.encrypt(first_name)
            last_name = self.encryption.encrypt(last_name)
            login = self.encryption.encrypt(login)
            password = self.encryption.hash(password)
        except Exception as e:
            print(e)

        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO `users` (`firstName`, `lastName`, `login`, `password`) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, login, password)
        )
        self.connection.commit()

    def login_db_check(self, login):

        cursor = self.connection.cursor()
        cursor.execute("SELECT login FROM users")

        results = cursor.fetchall()  # Returns a list of tuples, for example: [("login",),]

        for result in results:
            if self.encryption.decrypt(result[0]) == login:
                return False
        return True

    def login(self, username, password):
        pass

    def clear_table(self, table_name):

        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM {};".format(table_name))
        self.connection.commit()