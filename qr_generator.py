import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer

qr_data = input("Add what you want in the qr: ")
qr_name = input("What do you want it named as?: ")

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(qr_data)

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), )

img_1.save(f"{qr_name}.png")
