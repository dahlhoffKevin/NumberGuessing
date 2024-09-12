from cryptography.fernet import Fernet
import hashlib

class Security:
    def __init__(self, key=None):
        if key is None:
            self.key = self._load_key()
        else:
            self.key = key.encode()
        self.cipher_suite = Fernet(self.key)

    def _write_key(self):
        """Generiert einen Schluessel und speichert ihn in einer Datei."""
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

    def _load_key(self):
        """Laedt den Schluessel aus der Datei."""
        return open("key.key", "rb").read()

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
        
    @staticmethod
    def BuildHash(data: str) -> str:
        """Erstellt einen Hash-Wert aus einem String."""
        hash_object = hashlib.sha256(data.encode())
        return hash_object.hexdigest()