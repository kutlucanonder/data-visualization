import qrcode
from PIL import Image

data="https://github.com/kutlucanonder/data-visualization"

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=5,
)
qr.add_data(data)
img=qr.make_image().convert('RGB')
img=qr.make_image(fill_color="white",back_color="black")
logo=Image.open("./g1.png").resize((100,100)).convert("RGBA")

pos=(
    (img.size[0] - logo.size[0]) // 2,
    (img.size[1] - logo.size[1]) // 2
)


img.paste(logo,pos,logo)

img.save("can.png")

print("QR kodu başarıyla oluşturuldu.")