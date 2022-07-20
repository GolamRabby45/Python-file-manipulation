import PyPDF2

def read_pdf():
    with open('recipe-book.pdf', 'r+b') as f:
        reader = PyPDF2.PdfFileReader(f)
        print(reader.numPages)
        print(reader.getDocumentInfo())
        pageobj = reader.getPage(2)
        print("\n" + pageobj.extractText())

if __name__ == "__main__":
    read_pdf()
    


