#converts pdf, returns its text content as a string
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

def convert(fname, pages):
    if not pages:
        PAGE_NUMBERS = set()
    else:
        PAGE_NUMBERS = set(pages)

    OUTPUT = StringIO()
    MANAGER = PDFResourceManager()
    CONVERTOR = TextConverter(MANAGER, OUTPUT, laparams=LAParams())
    INTERPRETER = PDFPageInterpreter(MANAGER, CONVERTOR)

    PDF_FILE = open(fname, 'rb')
    for page in PDFPage.get_pages(PDF_FILE, PAGE_NUMBERS):
        INTERPRETER.process_page(page)
    PDF_FILE.close()
    CONVERTOR.close()
    text = OUTPUT.getvalue()
    OUTPUT.close
    return text 