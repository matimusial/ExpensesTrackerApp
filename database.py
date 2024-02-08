import mysql.connector
import bcrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

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

        try:
            first_name = self.encrypt(first_name)
            last_name = self.encrypt(last_name)
            login = self.encrypt(login)
            password = self.hash(password)
        except Exception as e:
            print(e)

        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO `users` (`firstName`, `lastName`, `login`, `password`) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, login, password)
        )
        self.connection.commit()

    def check(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT firstname from users where login = 'hehe'")
            result = cursor.fetchall()

            result = base64.b64decode(result[0][0])
            #print(type(result))
            result = self.decrypt(result)
            print(result)
        except Exception as e:
            print(e)

    def login_db_check(self, login):

        cursor = self.connection.cursor()
        cursor.execute("SELECT login FROM users")

        results = cursor.fetchall()  # Returns a list of tuples, for example: [("login",),]
        print(results)
        print(login)
        for result in results:
            if  self.decrypt(base64.b64decode(result[0])) == login: #
                return False
        return True

    def login(self, username, password):
        pass

    def hash(self, password):
        byte = password.encode('utf-8')
        hashed = bcrypt.hashpw(byte, bcrypt.gensalt())

        return base64.b64encode(hashed).decode('utf-8')

    def check_password(self, plain, hashed):

        byte_plain = plain.encode('utf-8')
        byte_hashed = base64.b64decode(hashed.encode('utf-8'))

        return bcrypt.checkpw(byte_plain, byte_hashed)

    def encrypt(self, data):

        key = self.read_key()

        cipher = AES.new(key, AES.MODE_CBC)

        data = data.encode('utf-8')

        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        ciphertext = cipher.iv + ciphertext

        return base64.b64encode(ciphertext).decode('utf-8')

    def decrypt(self, data):

        key = self.read_key()

        iv = data[:16]    # iv vector has 16 bytes
        ciphertext = data[16:]

        cipher = AES.new(key, AES.MODE_CBC, iv)

        original_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

        return base64.b64decode(original_data).decode('utf-8')

    def read_key(self):
        try:
            with open('key', 'r') as file:
                key = file.read()
        except Exception as e:
            print(e)
            return

        key = base64.b64decode(key)

        if len(key) != 24:
            print("Wrong AES-192 key_backup length")
            return
        return key

    def clear_table(self, table_name):

        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM {};".format(table_name))
        self.connection.commit()