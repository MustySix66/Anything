import PyPDF2

# Here goes the name of the encrypted PDF File 
PDF_Password = PyPDF2.PdfReader('Aversicierto.pdf')
# Next lane, we put the path of the word list we want to use
with open('passwords.txt','r',encoding='utf8') as f:
    for line in f:
        Password = line.strip()
        if PDF_Password.decrypt(Password) !=0:
            print(f"Password found: {Password}")
            break