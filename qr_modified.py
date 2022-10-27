from turtle import fillcolor
import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr.add_data("https://www.youtube.com/watch?v=2LaAJq1lB1Q&ab_channel=edureka%21")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("qrimg.png")