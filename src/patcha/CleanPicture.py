# -*- coding=UTF-8 -*-

#import pytesseract

from PIL import  Image
from pylab import  *

pathfile="G:\\picture\\a.png"



def test2():
    testfile="G:\\picture\\test.png"
    img =Image.open(pathfile)
    img=img.convert("L")
    w,h=img.size
    print("原始尺寸:%s %s"%(w,h))

    
    #裁剪成四张图片
    dex=w/4
    left,right=0,dex
    for i in range(4):
        print(left,right)
        box=(left,0,right,h)
        temp = img.crop(box)
        temp.save("G:\\picture\\"+str(i)+".png","png")
        left,right=right,right+dex
        
        


def test1():
    img =Image.open(pathfile)
    img = img.convert("L")
    imarr =array(img)
    print(imarr.shape,imarr.dtype)
    print(len(imarr))
    for x in imarr:
        for y in x:
            print(y,end=' ')
        print("\n")
            

        

def main():
    test1()
#     test2()

if __name__ == '__main__':
    main()