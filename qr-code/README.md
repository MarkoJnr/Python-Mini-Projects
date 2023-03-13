## QR Code Generator

This is a Python code that allows a user to enter a text or link and generates a QR code for it using the pyqrcode library. 

The generated QR code is then saved as a PNG file with the name 'qr_code.png' and a scale factor of 8.

The code first prompts the user to enter the text or link they want to generate a QR code for, and then uses the **pyqrcode.create()** function to generate a QR code object for the input data. 

The **.png()** method is then called on the QR code object to save it as a PNG file with the name 'qr_code.png' and the specified scale factor.

Note that in order to run this code, you will need to have the pyqrcode library installed in your Python environment.