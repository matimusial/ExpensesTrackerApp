import mysql.connector
import bcrypt
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class Database:

    """
    A class responsible for connecting to a MySQL database and performing operations on user data.
    """

    def __init__(self):

        self.url = "mysql://sql11682263:LVhJMjsENR@sql11.freesqldatabase.com/sql11682263"
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

        password = self.hash(password)

        try:
            first_name = self.encrypt(first_name)
            last_name = self.encrypt(last_name)
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
            if result[0] == login:
                return False
        return True

    def login(self, username, password, hashed):
        pass

    def hash(self, password):

        byte = password.encode('utf-8')
        hashed = bcrypt.hashpw(byte, bcrypt.gensalt())

        return hashed.decode('utf-8')

    def encrypt(self, data):

        try:
            with open('key.bin', 'rb') as file:
                key = file.read()
        except Exception:
            print("Wrong AES-192 key path")

        cipher = AES.new(key, AES.MODE_CBC)

        data = data.encode('utf-8')

        ciphertext = cipher.encrypt(pad(data, AES.block_size))

        return cipher.iv + ciphertext

    def decrypt(self):
        pass