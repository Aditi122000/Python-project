import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=2LaAJq1lB1Q&ab_channel=edureka%21")
img.save("qr_code.png")