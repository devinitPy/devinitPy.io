from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO
from pdfminer.converter import PDFPageAggregator

def pdfparser(path):
    pdf_file = file(path, 'rb')
    pdf_resource_manager = PDFResourceManager()
    #String buffer that will contain pdf data
    data_buffer = StringIO()
    codec = 'utf-8'
    #makes it possible to reflect pdf layout in returned data
    laparams = LAParams()
    #variable containing configurations for pdf converting
    configurations = TextConverter(pdf_resource_manager, data_buffer, codec=codec,laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(pdf_resource_manager, configurations)
    # Process each page contained in the document.
    for page in PDFPage.get_pages(pdf_file):
        interpreter.process_page(page)
        #data variable contain all the raw pdf data, Feel free to print it out
        data =  data_buffer.getvalue()

    return data



def manuplate_pdf_data(data):
    #split content by new line
    processed_data = data.splitlines()
    print  processed_data[0]

pdfdata = pdfparser("cv.pdf")
manuplate_pdf_data(pdfdata)
