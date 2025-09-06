# 🔐 TriDent Encryption

TriDent Encryption is a triple-layer encryption system that combines:
1. **Hex Editing**
2. **Bit Manipulation**
3. **Image-based Steganography**

It demonstrates how data can be securely transformed, scrambled, and hidden inside images, and then decoded back into its original form.

---

## 📂 Project Structure

```bash
trident-encryption/
│── README.md
│── requirements.txt
│
├── data/
│   ├── input_image.png          # Original input image
│   ├── encoded_image.png        # Image with hidden data
│   ├── hex_output.txt           # Hexadecimal output
│   ├── bit_output.txt           # Bit manipulation output
│   └── text_output.txt          # Final transformed text
│
├── src/
│   ├── code1_hex_editing.py         # Step 1: Hex editing
│   ├── code2_bit_manipulation.py    # Step 2: Bit manipulation
│   ├── code3_hex_to_text.py         # Step 3: Hex → Text
│   ├── code4_embed_text_in_image.py # Step 4: Embed text in image
│   ├── decode_image.py              # Decode embedded text
│   └── run_all.py                   # Run the full pipeline
│
└── docs/                            # Documentation (to be added later)
