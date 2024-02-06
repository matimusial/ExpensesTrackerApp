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

    def __del__(self):
        if self.connection.is_connected():
            self.connection.close()


    def register(self, firstName, lastName, login, password):

        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO `users` (`firstName`, `lastName`, `login`, `password`) VALUES (%s, %s, %s, %s)", (firstName, lastName, login, password))

        self.connection.commit()

    def loginDBCheck(self, login):

        cursor = self.connection.cursor()

        cursor.execute("SELECT login FROM users")

        results = cursor.fetchall() #returns list of tuples eg. [("login",),]

        for result in results:
            if result[0] == login: return False

        return True

        def login(self, username, password):
            pass

        def hash(self, password):
            pass

        def encrypt(self):
            pass

        def decrypt(self):
            pass