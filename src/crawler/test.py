# -*- coding=UTF-8 -*-


import pdfkit
from numpy.compat.setup import configuration
import os

def test1():
    options={
            "encoding":"UTF-8",
            "javascript-delay":1000
        }
    config = pdfkit.configuration(wkhtmltopdf=r"D:\SystemAssisTools\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_file("G:\\html\\霸王乌江自刎.html","G:\\txt\\test.pdf",options,configuration=config)

def test2():
    basePath="G:\\html\\"
    ls=[basePath+x for x in os.listdir(basePath)]
    options={
            "encoding":"UTF-8" ,
            "javascript-delay":1000           
    }
    config = pdfkit.configuration(wkhtmltopdf=r"D:\SystemAssisTools\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_file(ls,"G:\\txt\\test.pdf",options,configuration=config)


def test3():
    with open("G:\\txt\\test.txt","r+") as f:
        print(f.read())
def main():
    test3()
    
#wkhtmltopdf  G:\html\霸王乌江自刎.html G:\txt\test.pdf
if __name__ == '__main__':
    main()