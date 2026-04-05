import argparse
import qrcode

def generate_qr_code(url, output_path):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generate a QR code from a URL.")
    parser.add_argument("--url", required=True, help="URL to encode into the QR code")
    parser.add_argument("--output", default="qr.png", help="Output QR code image")

    args = parser.parse_args()

    print("Generating QR code...")
    output_file = generate_qr_code(args.url, args.output)
    print(f"Done! QR code saved to: {output_file}")


if __name__ == "__main__":
    main()
