from cryptography.fernet import Fernet


class Security:
    def __init__(self, key=None):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key.encode()  # Sicherstellen, dass der Schluessel als Bytes vorliegt
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, data: str) -> str:
        encrypted_data = self.cipher_suite.encrypt(data.encode())
        return encrypted_data.decode()

    def decrypt(self, encrypted_data: str) -> str:
        decrypted_data = self.cipher_suite.decrypt(encrypted_data.encode())
        return decrypted_data.decode()

    def is_encrypted(self, data: str) -> bool:
        try:
            self.cipher_suite.decrypt(data.encode())
            return True
        except:
            return False