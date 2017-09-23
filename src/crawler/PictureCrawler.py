# -*- coding=UTF-8 -*-


import requests
import re
import time
import os
import subprocess

basePath="G:\\picture\\xidian\\"

def crawl_picture():
    for i in range(100):
        response = requests.get("http://ids.xidian.edu.cn/authserver/captcha.html")
        with open("".join([basePath,str(i),".png"]),"wb") as f:
            f.write(response.content)
        time.sleep(5)


def changeFileFormat():
    for i in range(100):
        try:
            os.rename("".join([basePath,str(i),".png"]),"".join([basePath,str(i),".tif"]))
        except:
            pass

def makeBoxes():
    src="".join([basePath,"0",".tif"])
    des="".join([basePath,"xidian.font.exp","0"])
    status =subprocess.call("tesseract "+src+" "+des+" makebox")
    print(status)
    
def main():
#     crawl_picture()
#     changeFileFormat()
    makeBoxes()

if __name__ == '__main__':
    main()