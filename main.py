"""
📄 Project 8: QR Code Generator
👨‍💻 Created by: Hashir Adnan  
🌐 Website: www.techthf.xyz  
🗓️ Date: [Insert today's date]

🧠 Description:
This Python script generates a QR code from any text or URL and saves it as an image file.
It’s useful for creating shareable links, business cards, event passes, or contactless information.

📦 Features:
- Takes custom input (text, URL, etc.)
- Generates a high-quality QR code
- Saves it as a PNG image
- Simple and fast with no external API

🧰 Tools & Modules Used:
- qrcode: for generating QR code images
- PIL (optional): for advanced image handling

💡 How to Use:
1. Set the `data` variable with your desired text or URL.
2. Run the script using: `python main.py`
3. A file named `qr_code.png` will be created in the same folder.

✅ Example:
Input: "https://www.techthf.xyz"  
Output: qr_code.png (QR code for that URL)
"""

import qrcode

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,  # Version 1: 21x21 grid
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.show()  # This will display the QR code
    img.save('qr_code.png')  # This will save the QR code as an image file

data = 'https://www.example.com'
generate_qr_code(data)
