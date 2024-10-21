from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt data using AES
def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)  # AES in CBC mode
    iv = cipher.iv  # Initialization vector
    padded_text = pad(plaintext.encode('utf-8'), AES.block_size)  # Pad plaintext
    ciphertext = cipher.encrypt(padded_text)  # Encrypt the padded plaintext
    return iv + ciphertext  # Return IV + ciphertext together

# Function to decrypt data using AES
def aes_decrypt(key, ciphertext):
    iv = ciphertext[:16]  # Extract the first 16 bytes (IV)
    cipher = AES.new(key, AES.MODE_CBC, iv)  # AES in CBC mode with extracted IV
    decrypted_padded_text = cipher.decrypt(ciphertext[16:])  # Decrypt
    plaintext = unpad(decrypted_padded_text, AES.block_size)  # Unpad decrypted data
    return plaintext.decode('utf-8')

# Example usage
key = get_random_bytes(16)  # AES key (128 bits = 16 bytes)
plaintext = "Hello, AES encryption!"

# Encrypt the plaintext
ciphertext = aes_encrypt(key, plaintext)
print("Encrypted:", ciphertext)

# Decrypt the ciphertext
decrypted_text = aes_decrypt(key, ciphertext)
print("Decrypted:", decrypted_text)
