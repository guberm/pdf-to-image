#!/usr/bin/env python3
"""Convert PDF pages to JPEG images."""

from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Please install PyMuPDF: pip install pymupdf")
    exit(1)


def pdf_to_jpeg(pdf_path: str, dpi: int = 150) -> list[str]:
    """
    Convert each page of a PDF to a JPEG image.
    
    Creates a folder with the PDF name and saves images as name_1.jpg, name_2.jpg, etc.
    
    Args:
        pdf_path: Path to the PDF file
        dpi: Resolution for output images (default 150)
    
    Returns:
        List of paths to created JPEG files
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    
    # Create folder with PDF name in the same directory as the PDF
    output_dir = pdf_path.parent / pdf_path.stem
    output_dir.mkdir(parents=True, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    output_files = []
    
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap(matrix=matrix)
        
        # Save as pdfname_1.jpg, pdfname_2.jpg, etc.
        output_path = output_dir / f"{pdf_path.stem}_{page_num + 1}.jpg"
        pix.save(output_path, output="jpeg", jpg_quality=90)
        output_files.append(str(output_path))
        print(f"Saved: {output_path}")
    
    doc.close()
    return output_files


if __name__ == "__main__":
    # Ask for PDF path
    pdf_file = input("Enter full path to PDF file: ").strip()
    
    # Remove quotes if user included them
    pdf_file = pdf_file.strip('"').strip("'")
    
    if not pdf_file:
        print("No path provided.")
        exit(1)
    
    try:
        files = pdf_to_jpeg(pdf_file)
        print(f"\nConverted {len(files)} pages to: {Path(pdf_file).parent / Path(pdf_file).stem}/")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
