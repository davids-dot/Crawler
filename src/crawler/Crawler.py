# coding= UTF-8

import logging
import os
import re
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import pdfkit


class Crawler:
    HTML_TEMPLATE="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
    {content}
    </body>
    </html>
    """
    PAGE_ENCODING="UTF-8"

    @staticmethod
    def getResponse(url,**kwargs):
        return requests.get(url,**kwargs).content.decode(Crawler.PAGE_ENCODING)


    def __init__(self,start_url,name,saveHtmlDir="G:\\html\\",savePdfDir="G:\\txt\\",pageencoding="UTF-8",cssFilePath=None):
        Crawler.PAGE_ENCODING=pageencoding
        self.cssFilePath=cssFilePath
        self.start_url = start_url
        self.saveHtmlDir=saveHtmlDir
        self.savePdfDir=savePdfDir
        self.name=name
        self.initSoup()
        self.urls=[]  
        #其中存放的url是个bs4 中的Tag 对象，有属性href,string,
        self.domain ="{uri.scheme}://{uri.netloc}".format(uri=urlparse(start_url))

    def initSoup(self):
        self.soup =BeautifulSoup(Crawler.getResponse(self.start_url),"html.parser")


    def parse_menu(self):
        """
        :解析入口文档中的子网页url，并保存在self.urls中,每个网页
        :的名字保存在self.file_names 中
        """
        raise NotImplementedError

    def parse_body(self):
        raise NotImplementedError

    def crawl_file(self):
        """
        爬取网页到本地html文件
        """
        for a in self.urls:
            soup =BeautifulSoup(Crawler.getResponse(self.domain+a["href"]),"html.parser")
            html =self.parse_body(soup)
            filename =self.verifyName(a.string+".html")
            #此处有同名文件，会被覆盖，是一个bug
            with open(self.saveHtmlDir+filename,"wb") as file:
                file.write(bytes(html,"UTF-8"))

    
    def changeFileStruct(self,soup,title,pathfile):
        """
        为了打印出合理的pdf，更改html文件的结构
        """
        raise NotImplementedError

    def changeFiles(self):
        for a in self.urls:
            filename=self.verifyName(a.string)
            pathfile=self.saveHtmlDir+filename+".html"
            f=open(pathfile,"r+",encoding="UTF-8")
            soup =BeautifulSoup(f,"html.parser")
            html=self.changeFileStruct(soup,filename)
            f.close()
            with open(pathfile,"wb") as f:
                f.write(bytes(html,"UTF-8"))



    def verifyName(self,filename):
        """
        将在windows系统中不合法的字符转换
        """
        for ch in ["\\","/",":","?","*","\"","<",">","|"]:
            if filename.find(ch)!=-1:
                filename = filename.replace(ch,"_");
        return filename
        

    def verifyUrl(self,html):
        """
        将html 文档中的图片路径转换为
        """
        pattern ='(<img .*?src=")(.*?)(")'
                #第一个括号匹配img 之后，到src= 之间的所有内容,便于替换后再合成新url
                #第二个括号匹配任意字符的非贪婪模式。 *？，使*变成非贪婪模式
                # src" 之后， "之前的所有字符，即相对路径  m.group(2)
                #第三个括号匹配"号       m.group(3)
        def func(m):
            if not m.group(2).startswith("http"):
                rtn = "".join([m.group(1), self.domain, m.group(2), m.group(3)])
                return rtn
            else:
                return "".join([m.group(1), m.group(2), m.group(3)])
                #如果是绝对路径就再还原字符串

        html = re.compile(pattern).sub(func, html)
        #sub(pattern,repl,string,count=0,flags=0)
        #If repl is a function, it is called for every non-overlapping occurrence of #pattern. The function takes a single match object argument, and returns the 
        #replacement string. 
        return html

    def saveAsPdf(self):
        options={
            "encoding":"UTF-8",
            "javascript-delay":1000
        }
        config = pdfkit.configuration(wkhtmltopdf=r"D:\SystemAssisTools\wkhtmltopdf\bin\wkhtmltopdf.exe")
        ls=[self.saveHtmlDir+self.verifyName(x.string)+".html" for x in self.urls]
        pdfkit.from_file(ls,self.savePdfDir+self.name+".pdf",options,configuration=config)
        print(self.savePdfDir+self.name+".pdf")
    
    
    def getCss(self):
        if not self.cssFilePath==None:
            with open(self.cssFilePath,"r") as f:
                return f.read()
    
    def addCssFiles(self):
        css=self.getCss()
        for a in self.urls:
            filename=self.verifyName(a.string)
            pathfile=self.saveHtmlDir+filename+".html"
          
            f=open(pathfile,"r+",encoding="UTF-8")
            soup =BeautifulSoup(f,"html.parser")
            if soup.html==None:
                continue;
            contents=soup.html.head.contents
            last_tag=contents[len(contents)-1]
            style_tag=soup.new_tag("style")
            style_tag.append(css)
            last_tag.insert_after(style_tag)
            html=str(soup)
            f.close()
            with open(pathfile,"wb") as f:
                f.write(bytes(html,"UTF-8"))

    def test(self):
        print(self.urls[0])



def main():
    pass


if __name__ == "__main__":
    main()
        