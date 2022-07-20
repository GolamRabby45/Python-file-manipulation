import PyPDF2

def read_pdf():
    with open('recipe-book.pdf', 'r+b') as f:
        reader = PyPDF2.PdfFileReader(f)
        #print(reader.numPages)
        #print(reader.getDocumentInfo())

        for page in range(0, reader.numPages):
            pageobj = reader.getPage(page)
            print("\n" + pageobj.extractText())

if __name__ == "__main__":
    read_pdf()