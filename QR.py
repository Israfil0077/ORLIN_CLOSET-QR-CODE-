import qrcode

# Your link (replace this with your GitHub Pages URL)
url = "https://israfil0077.github.io/ORLIN_CLOSET-QR-CODE-/"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)
# Generate image (black & white)
img = qr.make_image(fill_color="black", back_color="white")

# Save file
img.save("qrcode.png")

# Save REAL PDF
img.save("qrcode.pdf", "PDF", resolution=300.0)

print("QR Code generated and saved as qrcode.png")