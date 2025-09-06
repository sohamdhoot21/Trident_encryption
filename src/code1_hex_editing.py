def text_to_hex(text):
    """
    Converts a text string to its hexadecimal representation.

    Parameters:
    - text (str): The text to convert.

    Returns:
    - str: The hexadecimal representation of the text.
    """
    hex_result = text.encode('utf-8').hex()
    return hex_result

# Get user input
user_text = input("Enter the text to encode: ")

# Convert the text to hex
hex_representation = text_to_hex(user_text)
print(f"Hexadecimal Representation: {hex_representation}")

# Save to a file for the next code
with open('hex_output.txt', 'w') as file:
    file.write(hex_representation)