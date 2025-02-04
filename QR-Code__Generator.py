import qrcode

URL = input("Enter the URL: ")

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=4,
)

qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.jpg")

print(qr.data_list)