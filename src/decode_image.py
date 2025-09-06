#!/usr/bin/env python3
import cv2

def decode_text_from_image(image_path):
    """
    Decodes a hidden text string from the RGB channels of an encoded image and reverses
    transformations (bit manipulation and hex editing) to reconstruct the original input.
    
    Parameters:
    - image_path (str): Path to the encoded image.
    
    Returns:
    - str: The original input string after reversing all transformations.
    """
    # Load the encoded image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image from {image_path}.")
        return

    print(f"Loaded encoded image with shape: {image.shape}")

    binary_text = ""

    print("Starting to decode text from the image...")

    # Iterate over the image pixels to decode the text
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            r, g, b = image[y, x]

            # Extract the LSB from each channel and append to the binary string
            binary_text += str(r & 1)  # LSB of red channel
            binary_text += str(g & 1)  # LSB of green channel
            binary_text += str(b & 1)  # LSB of blue channel

            # Check for the delimiter indicating the end of the message
            if binary_text[-16:] == '1111111111111110':  # 16-bit delimiter
                binary_text = binary_text[:-16]  # Remove the delimiter
                break
        else:
            continue
        break

    # Convert binary text back to the original string
    decoded_text = ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))
    print(f"Decoding complete. Decoded text: {decoded_text}")

    # Step 1: Reverse the bit manipulation (XOR operation)
    key = "secretkey"  # This should match the key used during encoding
    reversed_bit_text = xor_encrypt_decrypt(decoded_text, key)
    print(f"Text after reversing bit manipulation: {reversed_bit_text}")

    # Step 2: Reverse the hex editing
    try:
        original_text = hex_to_text(reversed_bit_text)
        print(f"Original input string: {original_text}")
    except ValueError:
        print("Error: The decoded text after bit manipulation is not a valid hex string.")
        original_text = reversed_bit_text
    
    return original_text

def xor_encrypt_decrypt(text, key):
    """
    Reverses the XOR operation on a text string using a given key.
    
    Parameters:
    - text (str): The text to decrypt.
    - key (str): The key used for encryption.
    
    Returns:
    - str: The decrypted text.
    """
    extended_key = (key * (len(text) // len(key) + 1))[:len(text)]
    result = ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, extended_key))
    return result

def hex_to_text(hex_string):
    """
    Converts a hexadecimal string back to the original text.

    Parameters:
    - hex_string (str): The hexadecimal string to convert.

    Returns:
    - str: The original text.
    """
    bytes_object = bytes.fromhex(hex_string)
    original_text = bytes_object.decode('utf-8')
    return original_text

# Example usage
encoded_image_path = 'encoded_image.png'

# Decode the text from the encoded image
decoded_message = decode_text_from_image(encoded_image_path)
print(f"Decoded message: {decoded_message}")
#reverse decoding.