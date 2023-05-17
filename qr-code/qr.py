import pyqrcode

data = "https://wellnessworkout.co.uk/"

# Using pyqrcode.create() to create a qr code of the input data 
qr = pyqrcode.create(data)

# Using .png method to save the qr code as PNG file of provided name & scale 
qr.png('qr_wellness.png', scale = 8)