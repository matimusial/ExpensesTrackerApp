import bcrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


class Encryption:
    def __init__(self):

        key_path = "secrets/aes_key"

        try:
            with open(key_path, 'r') as file:
                self.key = file.read()
            self.key = base64.b64decode(self.key)

            if len(self.key) != 24:
                raise ValueError("Wrong AES-192 key length")
        except Exception as e:
            raise Exception(f"Failed to initialize Encryption class: {e}")

    def hash(self, password):
        byte = password.encode('utf-8')
        hashed = bcrypt.hashpw(byte, bcrypt.gensalt())

        return base64.b64encode(hashed).decode('utf-8')

    def check_password(self, plain, hashed):

        byte_plain = plain.encode('utf-8')
        byte_hashed = base64.b64decode(hashed.encode('utf-8'))

        return bcrypt.checkpw(byte_plain, byte_hashed)

    def encrypt(self, data):

        cipher = AES.new(self.key, AES.MODE_CBC)

        data = data.encode('utf-8')

        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        ciphertext = cipher.iv + ciphertext

        return base64.b64encode(ciphertext).decode('utf-8')

    def decrypt(self, data):

        data = base64.b64decode(data)

        iv = data[:16]    # iv vector has 16 bytes
        ciphertext = data[16:]

        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        original_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

        return original_data.decode('utf-8')