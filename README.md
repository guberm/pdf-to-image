# PDF to Image Converter

Convert PDF pages into individual JPEG images with ease.

## Features

- Converts each PDF page to a separate JPEG image
- Customizable DPI/resolution for output quality
- Automatically creates an organized output folder
- Shows progress as files are saved
- Simple command-line interface

## Installation

### Requirements
- Python 3.7+

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pdf-to-image.git
cd pdf-to-image
```

2. Install dependencies:
```bash
pip install pymupdf
```

## Usage

Run the script and provide the path to your PDF file:

```bash
python "pdf to image.py"
```

Then enter the full path to your PDF file when prompted:
```
Enter full path to PDF file: C:\path\to\your\file.pdf
```

The script will:
- Create a folder named after your PDF (without extension)
- Convert each page to a JPEG image (name_1.jpg, name_2.jpg, etc.)
- Save all images in the created folder

### Customizing DPI

To use the function programmatically with custom DPI:

```python
from pdf_to_image import pdf_to_jpeg

# Convert with 300 DPI instead of default 150
files = pdf_to_jpeg("path/to/file.pdf", dpi=300)
print(f"Created {len(files)} images")
```

## Example

```bash
$ python "pdf to image.py"
Enter full path to PDF file: documents/manual.pdf
Saved: documents/manual/manual_1.jpg
Saved: documents/manual/manual_2.jpg
Saved: documents/manual/manual_3.jpg

Converted 3 pages to: documents/manual/
```

## License

MIT License - feel free to use and modify as needed.
