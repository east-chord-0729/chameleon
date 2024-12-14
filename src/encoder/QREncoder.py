from controller import windowController, messageController
from config import config
from PIL import Image, ImageTk
import qrcode


def generate_qrcode(data):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=2,
        border=1)
    qr.add_data(data)
    qr_image = qr.make_image(fill='black', back_color='white').convert('RGB')
    return qr_image


def update(root, label, info):
    message, mac = messageController.generate(info)
    qr_message, qr_mac = generate_qrcode(message), generate_qrcode(mac)
    size_qr, _ = qr_message.size

    width, height = windowController.get_size(root)
    qr_image = Image.new('RGBA', (width, height))
    numx, numy = width // size_qr + 1, height // size_qr + 1

    for y in range(numy):
        y1 = 32 + y * size_qr
        for x in range(numx):
            x1 = x * size_qr
            if (y + x) % 2:
                continue
            elif (y + x) % 4 == 2:
                qr_image.paste(qr_mac, (x1, y1))
            else:
                qr_image.paste(qr_message, (x1, y1))

    qr_image = ImageTk.PhotoImage(qr_image)
    label.config(image=qr_image)
    label.image = qr_image

    root.after(config.UPDATE_TIME, lambda: update(root, label, info))
    

def run(info):
    root = windowController.init("QR-Code Window", config.TRANSPARENCY_QR)
    label = windowController.init_label(root)
    update(root, label, info)
    root.mainloop()


if __name__ == "__main__":
    info = (config.HOST_NAME, config.AUDIENCE_NAME, config.HOST_KEY)
    run(info)