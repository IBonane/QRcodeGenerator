import qrcode
from qrcode.constants import ERROR_CORRECT_L

qrGenerate = qrcode.QRCode(
    version=3,
    error_correction=ERROR_CORRECT_L,
    box_size=3,
    border=5
)

info = input("Add your information : ")

qrGenerate.add_data(info)
qrGenerate.make(fit=True)

img = qrGenerate.make_image(fill_color="red", back_color="white")
img.save('code.png')

