import numpy as np
from sympy import Matrix

def mod_inverse(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    matrix_modulus_inv = (det_inv * Matrix(matrix).adjugate()) % modulus
    return np.array(matrix_modulus_inv).astype(int)

class HillCipher:
    def __init__(self, key_matrix):
        self.key_matrix = np.array(key_matrix)
        self.modulus = 26
        self.inverse_key_matrix = mod_inverse(self.key_matrix, self.modulus)

    def preprocess_text(self, text, size):
        text = text.replace(' ', '').lower()
        if len(text) % size != 0:
            text += 'x' * (size - len(text) % size)
        return text

    def text_to_matrix(self, text, size):
        matrix = []
        for i in range(0, len(text), size):
            row = [ord(char) - ord('a') for char in text[i:i + size]]
            matrix.append(row)
        return np.array(matrix).T

    def matrix_to_text(self, matrix):
        text = ""
        for i in range(matrix.shape[1]):
            for j in range(matrix.shape[0]):
                text += chr(int(matrix[j, i]) + ord('a'))
        return text

    def encrypt(self, plaintext):
        size = self.key_matrix.shape[0]
        plaintext = self.preprocess_text(plaintext, size)
        plaintext_matrix = self.text_to_matrix(plaintext, size)
        encrypted_matrix = np.dot(self.key_matrix, plaintext_matrix) % self.modulus
        return self.matrix_to_text(encrypted_matrix)

    def decrypt(self, ciphertext):
        size = self.key_matrix.shape[0]
        ciphertext_matrix = self.text_to_matrix(ciphertext, size)
        decrypted_matrix = np.dot(self.inverse_key_matrix, ciphertext_matrix) % self.modulus
        return self.matrix_to_text(decrypted_matrix)

# Example usage
if __name__ == "__main__":
    key_matrix = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]  # Example key matrix
    plaintext = input("Enter the plaintext: ")

    cipher = HillCipher(key_matrix)
    encrypted_text = cipher.encrypt(plaintext)
    decrypted_text = cipher.decrypt(encrypted_text)

    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

