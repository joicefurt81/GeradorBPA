import pdfplumber

pdf = pdfplumber.open('Layout_Exportacao_BPA.pdf')
for i, page in enumerate(pdf.pages):
    text = page.extract_text()
    if text:
        print(f'=== PAGE {i+1} ===')
        print(text)
        print()