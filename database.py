import mysql.connector


'''
This module connects to the MySQL database and stores the users data in users table.
In constructor there is connecting to database


'''

class Database:
    def __init__(self):
        self.url = "mysql://sql11682263:LVhJMjsENR@sql11.freesqldatabase.com/sql11682263"
        try:
            self.connection = mysql.connector.connect(
                host=self.url.split('@')[1].split('/')[0],
                user=self.url.split('://')[1].split(':')[0],
                password=self.url.split(':')[2].split('@')[0],
                database=self.url.split('/')[-1]
            )
        except mysql.connector.Error:
            self.error = "Błąd połaczenia z internetem, zrestartuj aplikację."

    def register(self, firstName, lastName, login, password):

        cursor = self.connection.cursor()

        # Na przykład wykonajmy prosty zapytanie SELECT
        cursor.execute(f"INSERT INTO `users` (`FirstName`, `LastName`, `Login`, `Password`) VALUES ('{firstName}', '{lastName}', '{login}', '{password}')")


        # Pobierz wyniki zapytania
        results = cursor.fetchall()

        print(type(results))


        # Wyświetl wyniki
        for row in results:
            print(row)

        # Nie zapomnij zamknąć połączenia, gdy skończysz pracę z bazą danych
        self.connection.close()

    def checkLogin(self, login):


        cursor = self.connection.cursor()

        cursor.execute("SELECT login FROM users")

        self.connection.close()

        results = cursor.fetchall() #returns list of tuples eg. [("login",),]

        for result in results:
            if result[0] == login: return False

        return True

        def login(self, username, password):
            pass

        def hash(self, password):
            pass