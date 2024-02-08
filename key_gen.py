import os
from Crypto.Random import get_random_bytes
import base64
from database import Database

filename = ["key", "key_backup/key_backup"]
AES_TYPE = 24
database = Database()

if input("Would you like to create a new key_backup, this will clear all user data? (y/n): ").lower() == "y":

    try:
        for i in filename:

            if os.path.exists(i):
                os.chmod(i, 0o755)
                os.remove(i)

            with open(i, 'w') as file:
                key = get_random_bytes(AES_TYPE)
                key = base64.b64encode(key).decode('utf-8')
                file.write(key)

            os.chmod(i, 0o400)


        print("New AES key_backup generated.")

        database.clear_table('users')
    except Exception as e:
        print(e)