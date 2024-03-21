import os
from Crypto.Random import get_random_bytes
import base64
from app.database.database import Database
from app.services.encryption import Encryption

mysql_url = "mysql://sql11682263:LVhJMjsENR@sql11.freesqldatabase.com/sql11682263"


def create_files(filename, text):
    for i in filename:
        # Checks if the file already exists, changes its permissions and deletes it
        if os.path.exists(i):
            os.chmod(i, 0o755)
            os.remove(i)

        # Creates a new file, writes the text, and sets the file to read-only
        with open(i, 'w') as file:
            file.write(text)
        os.chmod(i, 0o400)


def create_key(aes_type):
    filename = ["aes_key", "../secrets_backup/aes_key_backup"]
    if input("Would you like to create a new AES key, this will clear all user data and secret data. (y/n): ") == "y":
        database = Database()

        try:
            # Generates a random AES key, encodes it with base64, and writes it to files
            key = get_random_bytes(aes_type)
            key = base64.b64encode(key).decode('utf-8')
            create_files(filename, key)
            print("New AES key_backup generated.")
            database.clear_users_table()

        except Exception as e:
            print(e)


def create_secret(secret_name, text):
    filename = [f"{secret_name}", f"../secrets_backup/{secret_name}_backup"]
    encryption = Encryption()

    try:
        # Encrypts the provided text and saves it to specified files
        ciphertext = encryption.encrypt(text)
        create_files(filename, ciphertext)
        print("Text has been encrypted and saved.")

    except Exception as e:
        print(e)


# create_key(aes_type=24)
# create_secret("mysql_url", mysql_url)
