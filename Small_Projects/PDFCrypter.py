from PyPDF2 import PdfReader, PdfWriter

# Here goes the name of the PDF, I suggest it to be on the same directory
reader = PdfReader("paPDF.pdf")
writer = PdfWriter()
writer.append_pages_from_reader(reader)
# Here goes the password we want to add
writer.encrypt("kiralakilla")

# We will create another pdf crypted
with open("Aversicierto.pdf", "wb") as out_file:
    writer.write(out_file)
