import bcrypt, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class Encryption:
    """
    Class for encrypting and decrypting data and hashing passwords.
    It utilizes the bcrypt module to hash passwords and verify them.
    For data encryption and decryption, this class uses AES with a 192-bit (24-byte) key length (AES-192).
    The AES initialization vector (IV) is generated randomly for each encryption and prepended to the ciphertext.

    All methods returns string ciphertext sequentially:
        1. AES and bcrypt library returns byte
        2. base64 library returns encoded base64 byte
        3. .decode("utf-8") returns string
    """

    def __init__(self):
        """
        Initialization of the Encryption class.
        Reads the encryption key from a file. The key should be a base64-encoded string,
        24 bytes in length when decoded, which corresponds to AES-192.
        :raises ValueError: If the key is invalid.
        """
        key_path = "secrets/aes_key"

        try:
            with open(key_path, 'r') as file:
                self.key = base64.b64decode(file.read())

            if len(self.key) != 24:
                raise ValueError("Wrong AES-192 key length")
        except FileNotFoundError as e:
            raise FileNotFoundError("Encryption key file not found")
        except ValueError as e:
            raise ValueError(f"Failed to initialize Encryption class: {e}")

    def hash(self, password):
        """
        Hashes a password using bcrypt.
        :param password: (str) The password to hash.
        :return: (str) The hashed password, base64-encoded and utf-8-decoded.
        """
        byte = password.encode('utf-8')
        hashed = bcrypt.hashpw(byte, bcrypt.gensalt())
        return base64.b64encode(hashed).decode('utf-8')

    def check_password(self, plain, hashed):
        """
        Verifies a password against a hashed value.
        :param plain: (str) The plaintext password provided by the user.
        :param hashed: (str) The hashed password stored in the database.
        :return: (boolean) True if the passwords match, False otherwise.
        """
        byte_plain = plain.encode('utf-8')
        byte_hashed = base64.b64decode(hashed.encode('utf-8'))
        return bcrypt.checkpw(byte_plain, byte_hashed)

    def encrypt(self, data):
        """
        Encrypts data using AES-192. Each ciphertext is unique due to the random IV.
        :param data: (str) The data to be encrypted.
        :return: (str) The encrypted data, base64-encoded and utf-8-decoded.
        """
        cipher = AES.new(self.key, AES.MODE_CBC)
        data = data.encode('utf-8')
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        ciphertext = cipher.iv + ciphertext
        return base64.b64encode(ciphertext).decode('utf-8')

    def decrypt(self, data):
        """
        Decrypts data encrypted by the `encrypt` method. The IV is extracted from the beginning of the data,
        IV has 16 bytes.
        :param data: (str) The encrypted data, with the IV added, base64-encoded.
        :return: (str) The decrypted plaintext data.
        """
        data = base64.b64decode(data)
        iv = data[:AES.block_size]
        ciphertext = data[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        original_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return original_data.decode('utf-8')
