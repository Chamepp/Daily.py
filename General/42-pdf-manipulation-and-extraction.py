import PyPDF2

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except FileNotFoundError:
        print("File not found.")
    except PyPDF2.utils.PdfReadError:
        print("Error reading PDF.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide the path to your PDF file
pdf_file_path = "path/to/your/pdf/file.pdf"

# Call the function to extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_file_path)

# Print the extracted text
print(extracted_text)
