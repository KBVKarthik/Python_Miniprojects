import pyqrcode

data = input("Enter the text or link to generate QR code: ")

qr = pyqrcode.create(data)

qr.svg('qr_code.svg', scale = 8)
