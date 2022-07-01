import os
import pdftotext

# Data
pdf_path = input("Enter the path of the pdf file : ")

# Notify
assert os.path.exists(pdf_path), "this pdf file doesn't exist"

# Open File
with open(pdf_path, 'rb') as f_r:
    pdf_pages = pdftotext.PDF(f_r)

# Convert
for i, page in enumerate(pdf_pages):
    print('Page {}'.format(i))
    print(page)
    print('*'*100)
