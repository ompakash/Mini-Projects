# pip install segno
# pip install qrcode-artistic

import segno
from qrcode_artistic import write_artistic

qrcode_img = segno.make("This is QR generated",error='h')
write_artistic(qrcode_img,  background='Artistice QR code/tiger.webp', target='Artistice QR code/qr_tiger.png', scale=9)
