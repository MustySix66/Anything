from PyPDF2 import PdfReader, PdfWriter

def Crypter(pdfPath, pdfPassword):
    # Here goes the name of the PDF, I suggest it to be on the same directory
    reader = PdfReader(pdfPath)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    # Here goes the password we want to add
    writer.encrypt(pdfPassword)

    # We will create another pdf crypted
    with open("Aversicierto.pdf", "wb") as out_file:
        writer.write(out_file)

pdfPath = str(input("Please put the PDF path: "))
pdfPassword = str(input("Please put your desired password: "))
Crypter(pdfPath, pdfPassword)