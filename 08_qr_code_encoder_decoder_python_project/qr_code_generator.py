import qrcode 


def generate_qr(data, filename = "qr_code.png"):
    qr =    qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"QR Code saved as {filename}")


text = input("Enter Text or URL to encode: ")
generate_qr(text)