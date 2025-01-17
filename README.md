# **QR Forge - QR Code Generator**

**QR Forge** is a simple and user-friendly desktop application built with **Python** and **Tkinter**. It allows you to generate QR codes for any text or URL, customize the QR code's color, and save it as an image for future use.

---

## **Features** 🌟

- **Generate QR Codes**: Enter any text or link to instantly create a QR code.
- **Color Customization**: Choose from a variety of colors to personalize your QR code.
- **Save as Image**: Save the generated QR code as a `.png` file for reuse.
- **Intuitive Interface**: Clean and easy-to-navigate GUI.

---

## **Installation** ⚙️

### **Prerequisites**
- Python 3.6 or later
- Required libraries:
  - `tkinter` (built-in with Python on most systems)
  - `qrcode`
  - `Pillow`

### **Steps to Install**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/qr-forge.git
   cd qr-forge
   ```
2. Install dependencies:
   ```bash
   pip install qrcode[pil] Pillow
   ```
3. Run the application:
   ```bash
   python qr_forge.py
   ```

---

## **Usage** 🖥️

1. Launch the application.
2. Enter a URL or text in the input box.
3. Choose your preferred QR code color using the buttons on the left.
4. Click **Create** to generate the QR code.
5. To save the QR code, click the **Save** button. The QR code will be saved as `saved_qrcode.png` in the project directory.

---

## **Screenshots** 📸

Here’s how QR Forge looks in action:

![QR Forge Screenshot](https://github.com/user-attachments/assets/15420f6a-b8fa-4fa7-b821-70c19515abe9)

---

## **Project Structure** 📂

```
.
├── qr_forge.py         # Main Python script
├── QR_GEN/             # Folder for assets
│   ├── 1.ico           # Application icon
│   ├── kamekazi.png    # Default image
├── README.md           # Project documentation
```

---

## **Future Enhancements** 🚀
- Add support for different QR code sizes and formats.
- Enable error logging for better debugging.
- Support QR codes with embedded logos or icons.

---

## **Acknowledgments** 🤝
- **QR Code Generation**: Powered by the [qrcode](https://github.com/lincolnloop/python-qrcode) Python library.
- **Image Processing**: Handled using [Pillow](https://python-pillow.org/).

---

## **License** 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Let me know if you need further tweaks!
