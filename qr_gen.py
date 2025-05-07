import qrcode
from PIL import Image

def generate_qr(url: str, file_path: str):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # size of the QR code (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)
    print(f"QR code saved as: {file_path}")

# Example usage
if __name__ == "__main__":
    my_url = str(input("Enter your URL with https (https://www.google.com):"))
    file_path_with_name = str(input("Enter file path with name (example.png):"))
    print(f"Generated QR for {my_url}")
    generate_qr(my_url, file_path_with_name)
