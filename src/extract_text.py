from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

pdf_path = "data/VAT_Guide.pdf"  
text = extract_text_from_pdf(pdf_path)

with open("vat_text.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("Text extracted and saved to 'vat_text.txt'")
