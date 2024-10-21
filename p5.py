# Step 1: Install the pycryptodome library
# !pip install pycryptodome

# Step 2: Import required modules
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt data
def blowfish_encrypt(key, plaintext):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)  # ECB mode
    padded_text = pad(plaintext.encode('utf-8'), Blowfish.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

# Function to decrypt data
def blowfish_decrypt(key, ciphertext):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_padded_text, Blowfish.block_size)
    return plaintext.decode('utf-8')

# Example usage
key = get_random_bytes(16)  # Generate a random key (between 4 and 56 bytes)
plaintext = "Hello, Blowfish!"

# Encrypt the plaintext
ciphertext = blowfish_encrypt(key, plaintext)
print("Encrypted:", ciphertext)

# Decrypt the ciphertext
decrypted_text = blowfish_decrypt(key, ciphertext)
print("Decrypted:", decrypted_text)
