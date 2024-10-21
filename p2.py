import string

class PlayfairCipher:
    def __init__(self, key):
        self.key = key
        self.matrix = self.create_matrix(key)

    def create_matrix(self, key):
        key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates while preserving order
        key = key.replace('j', 'i')
        alphabet = string.ascii_lowercase.replace('j', '')  # Alphabet without 'j'
        matrix_key = key + ''.join([ch for ch in alphabet if ch not in key])

        matrix = []
        for i in range(5):
            row = list(matrix_key[i * 5:(i + 1) * 5])
            matrix.append(row)

        return matrix

    def preprocess_text(self, text):
        text = text.lower().replace('j', 'i')
        text = ''.join([ch for ch in text if ch in string.ascii_lowercase])

        processed_text = ""
        i = 0
        while i < len(text):
            processed_text += text[i]
            if i + 1 < len(text) and text[i] == text[i + 1]:
                processed_text += 'x'
            elif i + 1 < len(text):
                processed_text += text[i + 1]
                i += 1
            else:
                processed_text += 'x'
            i += 1

        return processed_text

    def find_position(self, char):
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return i, j
        raise ValueError(f"Character {char} not found in matrix")

    def process_pairs(self, text, encrypt=True):
        shift = 1 if encrypt else -1
        processed_text = ""

        for i in range(0, len(text), 2):
            a, b = text[i], text[i + 1]
            row1, col1 = self.find_position(a)
            row2, col2 = self.find_position(b)

            if row1 == row2:
                processed_text += self.matrix[row1][(col1 + shift) % 5]
                processed_text += self.matrix[row2][(col2 + shift) % 5]
            elif col1 == col2:
                processed_text += self.matrix[(row1 + shift) % 5][col1]
                processed_text += self.matrix[(row2 + shift) % 5][col2]
            else:
                processed_text += self.matrix[row1][col2]
                processed_text += self.matrix[row2][col1]

        return processed_text

    def encrypt(self, plaintext):
        plaintext = self.preprocess_text(plaintext)
        return self.process_pairs(plaintext, encrypt=True)

    def decrypt(self, ciphertext):
        return self.process_pairs(ciphertext, encrypt=False)


# Example usage
if __name__ == "__main__":
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")

    cipher = PlayfairCipher(key)
    encrypted_text = cipher.encrypt(plaintext)
    decrypted_text = cipher.decrypt(encrypted_text)

    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
