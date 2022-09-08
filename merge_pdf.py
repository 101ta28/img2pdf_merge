from pathlib import Path
import PyPDF2
import img2pdf
from PIL import Image
import shutil
import os
import webbrowser

# フォルダ内のPDFファイル一覧
pdf_dir = Path("./files")
img_dir = Path("./img")
img_files = sorted(img_dir.glob("*.jpg"))

def create_pdf():
    for i in range(len(img_files)):
        img = Image.open(img_files[i])
        pdf_bytes = img2pdf.convert(img.filename)
        file = open(f"{pdf_dir}/fix_{i}.pdf", "wb")
        file.write(pdf_bytes)
        file.close()
        img.close()

def merge_pdf():
    merged_pdf = PyPDF2.PdfFileMerger(strict=False)
    pdf_files = sorted(pdf_dir.glob("*.pdf"))

    for i in range(len(pdf_files)):
        merged_pdf.append(open(str(pdf_files[i]), "rb"))

    merged_pdf.write("merged.pdf")
    merged_pdf.close()

def delete_files():
    shutil.rmtree(pdf_dir)
    os.mkdir(pdf_dir)

def open_pdf():
    webbrowser.open("merged.pdf")

if __name__ == "__main__":
    create_pdf()
    merge_pdf()
    delete_files()
    open_pdf()
