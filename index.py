#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
from PyPDF2 import PdfFileReader


def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        for pg in range(pdf.numPages):
            page = pdf.getPage(pg)
            print (page)
            text = page.extractText()
            print (text)


if __name__ == '__main__':
    path = 'result_RET.pdf'
    page = text_extractor(path)
    print (page)