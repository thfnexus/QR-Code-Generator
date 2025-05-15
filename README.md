# 📄 QR Code Generator

**Created by:** Hashir Adnan  
🌐 [www.techthf.xyz](https://www.techthf.xyz)  
🗓️ May 14, 2025

---

## 🧠 Description

This Python script generates a QR code from any text, URL, or custom input and saves it as a PNG image file.  
It’s ideal for making shareable links, business cards, event passes, or any form of contactless information.

---

## 📦 Features

- ✍️ Accepts custom input (text, URL, contact info, etc.)  
- 🖼️ Generates high-quality QR code images  
- 💾 Saves the output as `qr_code.png`  
- ⚡ Fast, reliable, and does not rely on any external API

---

## 🧰 Tools & Modules Used

- `qrcode` — For generating the QR code  
- `PIL` *(optional)* — For advanced image control (used internally by `qrcode`)

---

## 💡 How to Use

1. Install the required package:
   ```bash
   pip install qrcode[pil]
