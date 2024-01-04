from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def agregar_firma(pdf_input_path, pdf_output_path, signature_path, location=(0, 0)):
    # Crear un nuevo archivo PDF con la firma
    c = canvas.Canvas('signature.pdf', pagesize=letter)
    c.drawImage(signature_path, location[0], location[1])
    c.showPage()
    c.save()

    # Fusionar el PDF de la firma con el PDF original
    pdf = PdfFileReader(pdf_input_path)
    signature = PdfFileReader('signature.pdf')
    pdf_writer = PdfFileWriter()

    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        if i == 0:  # Agregar la firma solo a la primera página
            page.mergePage(signature.getPage(0))
        pdf_writer.addPage(page)

    with open(pdf_output_path, 'wb') as fh:
        pdf_writer.write(fh)

# Ejemplo de uso
agregar_firma('original.pdf', 'firmado.pdf', 'firma.png', location=(300, 300))
