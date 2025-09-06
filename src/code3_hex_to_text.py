def hex_to_text(hex_string):
    """
    Converts a hex string back to the original text.

    Parameters:
    - hex_string (str): The hex string to convert.

    Returns:
    - str: The original text.
    """
    bytes_object = bytes.fromhex(hex_string)
    original_text = bytes_object.decode('utf-8')
    return original_text

# Load encrypted hex data from the previous code
with open('bit_output.txt', 'r') as file:
    encrypted_hex = file.read()

# Convert manipulated hex back to text
bit_manipulated_text = hex_to_text(encrypted_hex)
print(f"Text After Bit Manipulation: {bit_manipulated_text}")

# Save to a file for the next code
with open('text_output.txt', 'w') as file:
    file.write(bit_manipulated_text)