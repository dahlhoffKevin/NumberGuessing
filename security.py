from cryptography.fernet import Fernet
import hashlib

class Security:
    def __init__(self, key=None):
        if key is None:
            self.__key = self.__load_key()
        else:
            self.__key = key.encode()
        self.__cipher_suite = Fernet(self.__key)

    # def _write_key(self):
    #     """Generiert einen Schluessel und speichert ihn in einer Datei."""
    #     key = Fernet.generate_key()
    #     with open("key.key", "wb") as key_file:
    #         key_file.write(key)

    def __load_key(self):
        """Laedt den Schluessel aus der Datei."""
        return open("key.key", "rb").read()

    def encrypt(self, data: str) -> str:
        encrypted_data = self.__cipher_suite.encrypt(data.encode())
        return encrypted_data.decode()

    def decrypt(self, encrypted_data: str) -> str:
        decrypted_data = self.__cipher_suite.decrypt(encrypted_data.encode())
        return decrypted_data.decode()

    def is_encrypted(self, data: str) -> bool:
        try:
            self.__cipher_suite.decrypt(data.encode())
            return True
        except:
            return False
        
    @staticmethod
    def BuildHash(data: str) -> str:
        """Erstellt einen Hash-Wert aus einem String."""
        hash_object = hashlib.sha256(data.encode())
        return hash_object.hexdigest()
    
if __name__ == "__main__":
    security = Security()
    original_data = "Geheime Nachricht"
    encrypted_data = security.encrypt(original_data)
    print(f"Verschluesselte Daten: {encrypted_data}")

    decrypted_data = security.decrypt(encrypted_data)
    print(f"Entschluesselte Daten: {decrypted_data}")

    print(f"Ist verschluesselt: {security.is_encrypted(encrypted_data)}")
    print(f"Ist verschluesselt: {security.is_encrypted(original_data)}")

    # Verwendung der statischen Methode BuildHash
    hash_value = Security.BuildHash(original_data)
    print(f"Hash-Wert: {hash_value}")    