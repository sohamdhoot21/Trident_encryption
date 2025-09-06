import cv2
import numpy as np

def encode_text_to_image(input_image_path, output_image_path, text):
    """
    Encodes a text string into the RGB channels of an image.
    
    Parameters:
    - input_image_path (str): Path to the input image.
    - output_image_path (str): Path to save the encoded image.
    - text (str): The text to encode into the image.
    """
    # Load the image
    image = cv2.imread(input_image_path)
    if image is None:
        print(f"Error: Unable to load image from {input_image_path}.")
        return

    print(f"Loaded image with shape: {image.shape}")

    # Convert the text to binary representation and add a delimiter
    binary_text = ''.join(format(ord(char), '08b') for char in text) + '1111111111111110'  # Delimiter: '1111111111111110'
    binary_index = 0
    text_length = len(binary_text)

    print(f"Binary text length: {text_length} bits")

    # Check if the text can fit into the image
    max_capacity = image.shape[0] * image.shape[1] * 3  # Each pixel can store 3 bits (1 bit per channel)
    if text_length > max_capacity:
        print(f"Error: The text is too long to fit into the image. Max capacity is {max_capacity} bits.")
        return

    print("Starting to encode text into the image...")

    # Iterate over the image pixels to encode the text
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if binary_index < text_length:
                # Get the RGB values and ensure they are integers
                r, g, b = map(int, image[y, x])

                # Modify the LSB of each channel to store the text bits
                r = (r & 0xFE) | int(binary_text[binary_index])  # Update the LSB of red channel
                binary_index += 1

                if binary_index < text_length:
                    g = (g & 0xFE) | int(binary_text[binary_index])  # Update the LSB of green channel
                    binary_index += 1

                if binary_index < text_length:
                    b = (b & 0xFE) | int(binary_text[binary_index])  # Update the LSB of blue channel
                    binary_index += 1

                # Update the pixel values
                image[y, x] = [r, g, b]

                # Provide progress feedback for every 1000 bits encoded
                if binary_index % 1000 == 0:
                    print(f"Encoded {binary_index} bits...")

            else:
                break
        if binary_index >= text_length:
            break

    # Save the encoded image
    cv2.imwrite(output_image_path, image)
    print(f"Text encoded successfully. Saved to {output_image_path}")
    print(f"Total bits encoded: {binary_index}/{text_length} bits.")

# Load the final text from the previous code
with open('text_output.txt', 'r') as file:
    text_to_encode = file.read()

# Encode the text into the image
input_image_path = 'input_image.png'
encoded_image_path = 'encoded_image.png'
encode_text_to_image(input_image_path, encoded_image_path, text_to_encode)