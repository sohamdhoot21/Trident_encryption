# 🔐 TriDent Encryption

Triple-layer encryption system using:
	1.	Hex Editing
	2.	Bit Manipulation
	3.	Image-based Steganography

Securely transforms, scrambles, and hides data inside images, with decoding scripts to recover the original message.

⸻

# 📂 Project Structure
	•	data/ : Stores input, intermediate, and output files
	•	input_image.png : Original input image
	•	encoded_image.png : Image with hidden data
	•	hex_output.txt : Hexadecimal representation of input
	•	bit_output.txt : Bit-level transformed output
	•	text_output.txt : Final transformed text
	•	src/ : Contains Python scripts for encryption and decoding
	•	code1_hex_editing.py : Converts input text to hex
	•	code2_bit_manipulation.py : Performs bit-level transformations
	•	code3_hex_to_text.py : Converts hex back to readable text
	•	code4_embed_text_in_image.py : Embeds text into image
	•	decode_image.py : Extracts hidden data from encoded image
	•	run_all.py : Runs the complete encryption-decryption pipeline
	•	README.md : Project description and usage guide

⸻

# ✨ Features
	•	Converts plain text into hex, then applies bit manipulation.
	•	Embeds the transformed data securely inside an image file.
	•	Provides decoding to recover hidden data from encoded images.
	•	Modular scripts allow step-by-step or full-pipeline execution.

-----

 
# 🚀 How to use
Install Python dependencies:

# Clone repository
git clone https://github.com/your-username/trident-encryption.git
cd trident-encryption

# Install dependencies
pip install pillow numpy

# Run the full encryption pipeline
python src/run_all.py

# Decode hidden message from encoded image
python src/decode_image.py
