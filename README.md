Here’s a clean, professional, and developer‑friendly **README.md** for your project.  
It explains the purpose, installation, usage, and workflow in a way that makes the tool easy to understand for anyone who lands on the repo.

---

# 📘 **README.md**

```markdown
# Reference QR Code Generator

This project provides a simple command‑line tool for generating a QR code that links directly to a PDF containing academic references.  
Instead of trying to encode long reference text directly into a QR code (which exceeds QR capacity limits), the script generates a QR code that points to a **hosted PDF**—for example, a file stored on GitHub.

This approach ensures:
- Only **one** QR code is needed  
- The QR code remains **scannable on any device**  
- The full reference list is preserved in its original PDF format  
- No compression, splitting, or DataMatrix encoding is required  

---

## 🚀 Features

- Generate a QR code from any URL  
- Output a high‑resolution PNG image  
- Simple CLI interface  
- No Ghostscript dependency  
- Works offline once the QR code is generated  

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Swipesoft/blob_reference.git
cd blob_reference
pip install -r requirements.txt
```

The project uses:

- `qrcode` — pure Python QR code generator  
- `Pillow` — image processing backend  

---

## 🧰 Usage

### **Generate a QR code from a URL**

```bash
python main.py --url https://github.com/Swipesoft/blob_reference/raw/main/references.pdf --output references_qr.png
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--url` | Yes | The URL to encode into the QR code (e.g., a GitHub raw PDF link) |
| `--output` | No | Output filename for the QR code image (default: `qr.png`) |

---

## 📄 Example

To generate a QR code linking directly to your hosted references PDF:

```bash
python main.py --url https://github.com/Swipesoft/blob_reference/raw/main/references.pdf --output references_qr.png
```

This produces:

```
references_qr.png
```

Scanning the QR code will open the PDF immediately.

---

## 📝 Why Use a URL Instead of Encoding Text?

QR codes have strict size limits.  
A full academic reference list often exceeds **3 KB**, which is the maximum capacity of a QR code in binary mode.

By hosting the PDF online and encoding only the URL, you ensure:

- The QR code remains small and reliable  
- The full reference list is preserved  
- Scanning works instantly on any device  
- No need for DataMatrix or compression tricks  

---

## 📂 Project Structure

```
.
├── main.py            # QR code generator script
├── requirements.txt   # Python dependencies
├── references.pdf     # Example reference file (hosted on GitHub)
└── README.md          # Project documentation
```

---

## 🤝 Contributing

Pull requests are welcome.  
If you want to extend the tool (e.g., embed QR codes into PDFs, validate URLs, or support DataMatrix), feel free to open an issue.

---

## 📄 License

MIT License.  
You are free to use, modify, and distribute this tool.

```

