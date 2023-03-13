import pyqrcode

data = input("Enter the text or link to generate QR code: ")

# Using pyqrcode.create() to create a qr code of the input data 
qr = pyqrcode.create(data)

# Using .png method to save the qr code as PNG file of provided name & scale 
qr.png('qr_code.png', scale = 8)