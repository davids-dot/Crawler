# -*- coding: UTF-8 -*-


from bs4 import BeautifulSoup


class Namer:
    
    def __init__(self,pathfile):
        self.pathfile=pathfile
        with open(pathfile,"r+",encoding="UTF-8") as f:
            self.soup=BeautifulSoup(f,"html.parser")
        
    
  
    def doType1(self, tag):
            label =tag.label
            if label ==None:
                return
            name =label.string
            if name==None:
                return
            name=name.strip()
            name=name.replace("：","") 
            name=name.replace(":","")
            label["for"]=name     
            input_tag=tag.input
            if input_tag==None:
                return
            input_tag["name"]=name
            input_tag["id"]=name
            
            
    
    
    def doType2(self, tag):
        label = tag.label
        if label == None:
            return 
        prefix =label.string.strip()
        prefix =prefix.replace("：",":")
        if ":" not in prefix:
            prefix="".join([prefix,":"])
        cbxs =tag.find_all("div","cbx")
        for cbx in cbxs:
            cb_label=cbx.label
            if cb_label ==None:
                continue
            cb_str=cb_label.string
            if cb_str==None:
                continue
            cb_input=cbx.input
            if cb_input==None:
                continue
            cb_name=prefix+cb_str.strip()
            cb_label["for"]=cb_name
            cb_input["id"]=cb_name
            cb_input["name"]=cb_name
        #以下部分未实验
       
            
        
        
    
    
    def test(self):
        ls = self.soup.select(".formControls")
        for con in ls:
            childNo = len(con.contents)
            if childNo==4:
                self.doType1(con)
            else:
                self.doType2(con)
        print(str(self.soup))
        with open(self.pathfile,"wb") as f:
            f.write(bytes(self.soup.prettify(),"UTF-8"))
      


def main():
    pathfile="".join([r"G:\XiangXiHospital\src\05-webEmr\页面待开发部分",
    r"\WebEmr\view\PICC\PICCPreplacementAssessment\PICCPreplacementAssessment.html"])
    namer = Namer(pathfile)
    namer.test()
    
    

if __name__ == '__main__':
    main()