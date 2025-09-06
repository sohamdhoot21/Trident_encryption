def xor_encrypt_decrypt(hex_text, key):
    """
    Encrypts or decrypts a hex string using a given key with XOR operation.

    Parameters:
    - hex_text (str): The hex string to encrypt or decrypt.
    - key (str): The key to use for encryption or decryption.

    Returns:
    - str: The resulting encrypted or decrypted hex string.
    """
    extended_key = (key * (len(hex_text) // len(key) + 1))[:len(hex_text)]
    result = ''.join(format(ord(t) ^ ord(k), '02x') for t, k in zip(hex_text, extended_key))
    return result

# Load hex data from the previous code
with open('hex_output.txt', 'r') as file:
    hex_text = file.read()

# Define key for bit manipulation
key = "secretkey"

# Perform XOR encryption/decryption
encrypted_hex = xor_encrypt_decrypt(hex_text, key)
print(f"Bit Manipulated Hex: {encrypted_hex}")

# Save to a file for the next code
with open('bit_output.txt', 'w') as file:
    file.write(encrypted_hex)