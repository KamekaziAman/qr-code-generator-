QR Forge - QR Code Generator
QR Forge is a user-friendly desktop application built with Python and Tkinter that allows you to generate QR codes for any text or link. You can also customize the QR code's color and save it as an image for later use.

Features
QR Code Generation: Enter any text or URL to create a QR code instantly.
Color Customization: Choose from multiple colors to personalize your QR code.
Save QR Code: Save the generated QR code as an image file (saved_qrcode.png).
Simple Interface: A clean and intuitive GUI for easy interaction.
Installation
Prerequisites
Python 3.6 or above
Required Python libraries:
tkinter
qrcode
Pillow
![image](https://github.com/user-attachments/assets/15420f6a-b8fa-4fa7-b821-70c19515abe9)

git clone https://github.com/yourusername/qr-forge.git
cd qr-forge

pip install qrcode[pil] Pillow

How to Use
Launch the application.
Enter the text or URL in the input field.
Choose a border color from the palette.
Click the Create button to generate the QR code.
To save the QR code, click the Save button. The QR code will be saved as saved_qrcode.png in the current directory.

.
├── qr_forge.py         # Main Python script
├── QR_GEN/             # Folder for assets
│   ├── 1.ico           # Application icon
│   ├── kamekazi.png    # Default image
├── README.md           # Project documentation


Future Enhancements
Add support for different QR code sizes.
Implement error logging.
Include support for generating QR codes with logos.
Acknowledgments
QR code generation is powered by the qrcode Python library.
Image processing is handled using Pillow.
License
This project is licensed under the MIT License - see the LICENSE file for details.
