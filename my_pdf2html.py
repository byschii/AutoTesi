from pdfminer.tools import pdf2txt

def extract(inputFile, outputFile):
   pdf2txt.main(["pdf2txt","-o", outputFile, inputFile])

if __name__ == '__main__': 
    extract('input.pdf', 'output.html')
